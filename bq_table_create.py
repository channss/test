from google.cloud import bigquery

def create_bigquery_table(project, dataset, table):
    # Create a BigQuery client
    client = bigquery.Client(project=project)

    # Define the table schema
    schema = [
        bigquery.SchemaField('partition', 'INT64'),
        bigquery.SchemaField('offset', 'INT64'),
        bigquery.SchemaField('key', 'STRING'),
        bigquery.SchemaField('value', 'BYTES'),
        bigquery.SchemaField('event_create_time', 'TIMESTAMP'),
    ]

    # Define the table reference
    table_ref = client.dataset(dataset).table(table)

    # Define the table options
    table_options = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field='event_create_time'
    )

    # Define the table schema and options
    table = bigquery.Table(table_ref, schema=schema)
    table.time_partitioning = table_options
    table.clustering_fields = ['partition', 'key']

    # Create the table
    table = client.create_table(table)

    print(f'Table {table.table_id} created successfully.')


if __name__ == '__main__':
    project = 'wanted-data-nw'
    dataset = 'log_streaming_test'

    lst = [
        'gigs-api-nextweek-log',
        'pie-openapi-web-nextweek-log',
        'pie-wanted-web-nextweek-log',
        'python2-wanted-web-nextweek-log',
        'wanted-oneid-backend-nextweek-log'
    ]

    for e in lst:
        create_bigquery_table(project, dataset, e)