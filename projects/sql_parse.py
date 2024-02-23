import re
from sql_metadata import Parser
from melting_pot.google import gbq, load_client, safe_send_bigquery
from google.cloud import bigquery

def get_audit_data():
    sql = """
    with raw as (
    SELECT
        protopayload_auditlog.resourceName,
        protopayload_auditlog.methodName,
        JSON_VALUE(protopayload_auditlog.metadataJson, '$.tableCreation.table.view.query') query,
        JSON_VALUE(protopayload_auditlog.metadataJson, '$.tableChange.table.view.query') query2,
        timestamp,
        rank() over (partition by protopayload_auditlog.resourceName order by timestamp desc) rnk
    FROM `audit.cloudaudit_googleapis_com_activity`
    WHERE protopayload_auditlog.methodName <> "google.cloud.bigquery.v2.TableService.DeleteTable"
    )

    select
        resourceName,
        # methodName,
        case when query is null then query2 else query end as query,
        # timestamp
    from raw
    where rnk = 1
    and (query is not null or query2 is not null)
    """
    df = gbq(sql, stage='www')
    return df

def get_source_tables_from_query(sql, datasets):
    s = re.sub(r'\#.+?(\n+)', '', sql)
    parser = Parser(s)

    p = re.compile(r'[\w-]+\.[\w.\s-]+')
    tables = [t for t in parser.tables if p.match(t)]
    return remove_non_tables(datasets, tables)

# jongwony
def get_source_tables_regex_jongwony(query, datasets):
    q = re.sub(r'(\#|\-\-).+?(\n+)', '', query)
    pattern = r'(?:FROM|JOIN)([`"\'\s])*(.*?)(\1|\s|$)'
    table_names = re.findall(pattern, q, flags=re.IGNORECASE | re.MULTILINE)
    tns_lst = [t[1].strip(');,') for t in table_names]
    p = re.compile(r'^.*`')
    tns_set = set([m.group(0) if (m := re.search(r'^.*`', t)) else t for t in tns_lst])
    return [t for t in tns_set if len(t.split('.')) > 1 and t.replace('`', '').split('.')[-2] in datasets]


def get_source_tables_regex(query, datasets):
    q = re.sub(r'(\#|\-\-).+?(\n+)', '', query)
    pattern = r'(?i)(?:FROM|JOIN)\s*([^\s,);]+)'
    table_names = re.findall(pattern, q, flags=re.IGNORECASE | re.MULTILINE)
    tns = set([table_name_test(t) for t in table_names])
    lst = [t.replace('`','') for t in tns]
    p = re.compile(r'[\w-]+\.[\w.\s-]+')
    tables = [t for t in lst if p.match(t)]
    return remove_non_tables(datasets, tables)

def table_name_test(t):
    for i in range(len(t)):
        if t[i] == '`':
            if i == len(t)-1:
                continue
            elif i == 0:
                continue
            elif t[i+1] == '.':
                continue
            elif t[i-1] == '.':
                continue
            else:
                return t[0:i+1]
    return t

def remove_non_tables(datasets, tables):
    return [t for t in tables if t.split('.')[-2] in datasets]


def get_destination_table(tableName):
    d = re.compile(r'(?<=datasets/)[\w_-]+')
    t = re.compile(r'(?<=tables/)[\w_-]+')
    return '.'.join([d.search(tableName)[0], t.search(tableName)[0]])


def list_datasets():
    client = load_client(bigquery, stage='www')
    datasets = list(client.list_datasets())

    return set([ds.dataset_id for ds in datasets])


if __name__ == '__main__':
    targets = get_audit_data()
    datasets = list_datasets()

    targets['regex'] = targets['query'].apply(lambda x: set(get_source_tables_regex(x, datasets)))
    targets['jongw'] = targets['query'].apply(lambda x: set(get_source_tables_regex_jongwony(x, datasets)))
    # targets['sqlmd'] = targets['query'].apply(lambda x: set(get_source_tables_from_query(x, datasets)))
    targets['common'] = targets.apply(lambda x: set.intersection(x['regex'], x['jongw']), axis=1)
    targets['xor'] = targets.apply(lambda x: set.symmetric_difference(x['regex'], x['jongw']), axis=1)
    # targets['cj_xor'] = targets.apply(lambda x: set.symmetric_difference(x['regex'], x['jongwony']), axis=1)

    filtered = targets[targets['xor'].apply(bool)]
