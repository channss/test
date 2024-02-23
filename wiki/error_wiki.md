### 카프카 메세지 유니코드 변환 에러
---

### 내용 요약
weaver_log consumer에서 카프카 메세지를 string으로 변환 중 특수문자를 파싱할 수 없어 발생한 에러.

### 프로젝트 keywords
weaver, kafka, consumer, firelens

### 종류
에러, UnicodeDecodeError

### 발생 일시
2023-05-24

### 배경/원인 및 세부 내용
firelens_gigs-api-www-log 컨슈머에서 메세지를 읽던 중 byte 형식의 [카프카 메세지 value](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#confluent_kafka.Message.value)를 string으로 decode하는데, 특수문자를 인식하지 못해서 발생한 에러. Byte를 string으로 변환한 이유는, 빅쿼리에서 내용을 알아볼 수 있기 때문. Byte는 사람이 읽을 수 없는 문자열로 저장이 된다.

문제가 value를 포함한 에러 메세지는 아래와 같음:
```shell
pyarrow.lib.ArrowInvalid: Could not convert b'{"@timestamp":1684303406.248044,"timestamp":"2023-05-17 15:03:26","elapsed_time":0.1520562171936035,"user_id":2606034,"req_method":"POST","req_path":"/api/chaos/community/v2/posts","req_path_distinct":"/api/chaos/community/v2/posts","req_client_ip":"211.234.198.84","req_headers":{"Host":"www.wanted.co.kr","User-Agent":"Wanted/11.0.0 (com.wantedlab.wanted; build:230511003; iOS 16.4.1) Alamofire/5.6.1","Authorization":null,"Content-Type":"application/json","Referer":null,"WANTED-User-Country":"KR","WANTED-User-language":"ko","WANTED-User-Agent":"iOS_11.0.0","WANTED-Ad-Id":"00000000-0000-0000-0000-000000000000","WANTED-Simsmode":null},"req_cookies":{"WWW_ONEID_ACCESS_TOKEN":"1af0452cb06e422b8f5dbf92669c244f","WWW_HQ_ONEID_ACCESS_TOKEN":null},"req_querystring":{},"req_body":{"content":"\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94!\\n\xec\xb7\xa8\xec\x97\x85&\xec\x9e\xac\xec\xb7\xa8\xec\x97\x85 \xed\x99\x9c\xeb\x8f\x99\xec\x9d\x84 \xed\x95\x98\xea\xb3\xa0\xec\x9e\x88\xeb\x8a\x94 \xec\x82\xac\xeb\x9e\x8c\xeb\x93\xa4\xec\x9d\x98 \xec\xbb\xa4\xeb\xae\xa4\xeb\x8b\x88\xed\x8b\xb0\xeb\xa5\xbc \xec\xa4\x80\xeb\xb9\x84\xec\xa4\x91\xec\x9e\x85\xeb\x8b\x88\xeb\x8b\xa4! \\n\xec\x9d\xb4 \xed\x94\x84\xeb\xa1\x9c\xec\xa0\x9d\xed\x8a\xb8\xeb\xa1\x9c \xec\x88\x98\xec\x9d\xb5\xea\xb9\x8c\xec\xa7\x80 \xeb\x82\xb4\xeb\xb3\xb4\xeb\x8a\x94 \xea\xb2\x83\xec\x9d\x84 \xeb\xaa\xa9\xed\x91\x9c\xeb\xa1\x9c \xed\x95\x98\xea\xb3\xa0 \xec\x9e\x88\xec\x9c\xbc\xeb\xa9\xb0 \\n\xea\xb3\x84\xec\x86\x8d\xed\x95\xb4\xec\x84\x9c \xec\x9c\xa0\xec\xa7\x80\xeb\xb3\xb4\xec\x88\x98\xeb\xa5\xbc \xed\x95\xb4\xea\xb0\x80\xeb\xa9\xb0 \xed\x95\xa8\xea\xbb\x98 \xeb\x8b\xb5\xec\x9d\x84 \xec\xb0\xbe\xec\x95\x84\xea\xb0\x88 \xec\x98\x88\xec\xa0\x95\xec\x9e\x85\xeb\x8b\x88\xeb\x8b\xa4. \\n\\n\xec\xa7\x81\xea\xb5\xb0, \xea\xb2\xbd\xed\x97\x98, \xea\xb2\xbd\xeb\xa0\xa5 \xeb\xac\xb4\xea\xb4\x80\xed\x95\x98\xeb\xa9\xb0 \xed\x95\x98\xea\xb3\xa0\xec\x9e\x90\xed\x95\x98\xeb\x8a\x94 \xec\x97\xb4\xec\xa0\x95 \xea\xb0\x80\xeb\x93\x9d\xed\x95\x98\xec\x8b\xa0 \xeb\xb6\x84\xeb\x93\xa4\xed\x99\x98\xec\x98\x81\xec\x9e\x85\xeb\x8b\x88\xeb\x8b\xa4. \\n\\n\xeb\xac\xb8\xec\x9d\x98\xeb\x8a\x94 \xec\x95\x84\xeb\x9e\x98 \xeb\xa7\x81\xed\x81\xac\xeb\xa1\x9c \xeb\xb6\x80\xed\x83\x81\xeb\x93\x9c\xeb\xa0\xa4\xec\x9a\x94! \\n\\n\xec\xb9\xb4\xec\xb9\xb4\xec\x98\xa4\xed\x86\xa1 \xec\x98\xa4\xed\x94\x88\xec\xb1\x84\xed\x8c\x85\xec\x9d\x84 \xec\x8b\x9c\xec\x9e\x91\xed\x95\xb4 \xeb\xb3\xb4\xec\x84\xb8\xec\x9a\x94.\\n\xeb\xa7\x81\xed\x81\xac\xeb\xa5\xbc \xec\x84\xa0\xed\x83\x9d\xed\x95\x98\xeb\xa9\xb4 \xec\xb9\xb4\xec\xb9\xb4\xec\x98\xa4\xed\x86\xa1\xec\x9d\xb4 \xec\x8b\xa4\xed\x96\x89\xeb\x90\xa9\xeb\x8b\x88\xeb\x8b\xa4.\\n\\n\xec\x82\xac\xec\x9d\xb4\xeb\x93\x9c\xed\x94\x84\xeb\xa1\x9c\xec\xa0\x9d\xed\x8a\xb8\\nhttps://open.kakao.com/o/smSgKvkf\\n\\n\xea\xb0\x90\xec\x82\xac\xed\x95\xa9\xeb\x8b\x88\xeb\x8b\xa4 \xed\xa0\xbd\xed\xb8\x80","image_ids":[],"tag_type_ids":[10241,10093,10075],"title":"\xec\x83\x88\xeb\xa1\x9c\xec\x9a\xb4 \xed\x94\x84\xeb\xa1\x9c\xec\xa0\x9d\xed\x8a\xb8 \xed\x8c\x80\xec\x9b\x90 \xeb\xaa\xa8\xec\xa7\x91\xed\x95\xa9\xeb\x8b\x88\xeb\x8b\xa4","meta_tag_ids":[694]},"resp_status_code":200,"user":{"id":2606034,"company_id":null,"country":"KR","languages":["ko","en"],"simsmode_admin":null,"agent_header":"iOS_11.0.0","oneid":"BDbbn8HpHqeCEZ6cwuRzBf","access_token":"1af0452cb06e422b8f5dbf92669c244f","company_role":null},"server_host":"wanted-server-www","server_private_ip":"10.10.2.231","server_stage":"WWW","simsmode_admin":null,"server_version":"python3","level":"OK","dd":{"trace_id":"5186177480135091526","span_id":"7375893575676281240","env":"www","service":"pie-wanted-web","version":"Release_20230511_02"},"container_id":"cfc02361013446448c76800aa382e198-2367003168","container_name":"wanted-server-www","source":"stdout","ecs_cluster":"wanted-www-cluster","ecs_task_arn":"arn:aws:ecs:ap-northeast-2:308690228324:task/wanted-www-cluster/cfc02361013446448c76800aa382e198","ecs_task_definition":"wanted-server-www:218","service":"pie-wanted-web"}' with type bytes: was not a utf8 string

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 125: invalid continuation byte
```
위 메세지의 `\xed\xa0\xbd\xed\xb8\x80` 부분을 decode할 수 없어 에러 발생. 이 문자열은 😁 와 비슷한 이모티콘으로 확인.

### 해결방식
처음 문제를 발견했을 당시인 2023-05-24에는 string으로 변환하는 코드를 다음과 같이 수정했음: `msg.value().decode()` -> `msg.value().decode(errors='replace')`. 이렇게 하면 decode 중 발생하는 에러는 특수문자(�)로 치환하기 때문.
하지만 이후 비슷한 문제가 2023-06-10에 다시 발생했을 때는 빅쿼리 schema를 string에서 byte로 변경해 아예 decoding을 하지 않는 방법을 선택함. 이유는 api, client 등에서 발생하는 로그를 수집하는 것이 목적인데, 그것을 온전히 받아서 저장하는게 아닌 data loss를 감수하면서 변환시켜 저장하는 것이 잘못되었다고 생각했기 때문.  
이모티콘 등의 특수문자를 포기하더라도 msg.value()를 변환해 저장하는 기존의 코드:
```python
def parse_logs(msg, exec_time):
    value = msg.value().decode(errors='replace')
    return {
        'partition': msg.partition(),
        'offset': msg.offset(),
        'key': msg.key(),
        'value': value,
        'event_create_time': datetime.utcfromtimestamp(json.loads(value)['@timestamp']),
        'update_time': exec_time,
    }


def gbq_message_schema():
    schema = {
        'partition': 'INT64',
        'offset': 'INT64',
        'key': 'STRING',
        'value': 'STRING',
        'event_create_time': 'TIMESTAMP',
        'update_time': 'TIMESTAMP',
    }
    return [
        bigquery.SchemaField(k, v)
        for k, v in schema.items()
    ]
```
빅쿼리에서 바로 보기는 어렵더라도 msg.value()를 변환하지 않고 byte로 온전히 저장하는 신규 코드.
```python
def parse_logs(msg, exec_time):
    return {
        'partition': msg.partition(),
        'offset': msg.offset(),
        'key': msg.key(),
        'value': msg.value(),
        'event_create_time': datetime.utcfromtimestamp(json.loads(msg.value().decode(errors='replace'))['@timestamp']),
        'update_time': exec_time,
    }


def gbq_message_schema():
    schema = {
        'partition': 'INT64',
        'offset': 'INT64',
        'key': 'STRING',
        'value': 'BYTES',
        'event_create_time': 'TIMESTAMP',
        'update_time': 'TIMESTAMP',
    }
    return [
        bigquery.SchemaField(k, v)
        for k, v in schema.items()
    ]
```
