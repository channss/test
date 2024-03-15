import boto3
import requests


def call_wanted_api(method, path, **kwargs):
    return requests.request(
        method=method,
        url=f"{LAAS_BASE_URL}{path}",
        headers={
            "project": "WANTED_DATA",
            "apiKey": LAAS_API_KEY,
            "Content-Type": "application/json; charset=utf-8",
        },
        **kwargs,
    )


def vector_discovery(collections, query, limit, filter_query=None):
    q = {
        'text': query,
        'limit': limit,
        'offset': 0,
        'with_metadata': True,
        'with_vector': False,
    }
    if filter_query:
        q['filter'] = filter_query

    return call_wanted_api(
        'POST',
        f'/api/document/{collections}/similar/text',
        json=q,
    )


def get_parameter(key):
    ssm = boto3.client('ssm', region_name='ap-northeast-2')
    return ssm.get_parameter(Name=key, WithDecryption=True)['Parameter']['Value']


LAAS_BASE_URL = 'https://api-laas.wanted.co.kr'
LAAS_API_KEY = get_parameter('/DATA/PIPELINE/API_KEY/OPENAI')
ATLASSIAN_API_KEY = get_parameter('/DATA/ATLASSIAN/API_KEY/JONGWON')
