import boto3
import requests
import hashlib

from melting_pot.google import gbq
from projects.laas import StageABC


class Env(StageABC):
    _stage = {
        'nextweek': 'nw',
        'www': 'www',
    }


def get_parameter(key):
    ssm = boto3.client('ssm', region_name='ap-northeast-2')
    return ssm.get_parameter(Name=key, WithDecryption=True)['Parameter']['Value']


def hashing(string):
    return int.from_bytes(
        hashlib.sha256(string.encode()).digest()[:4]
    )


def get_skills():
    return gbq("""
        select distinct content
        from `wanted-data-nw.temp.chann_skill_test`
    """, Env.config("_stage"))


def call_wanted_api(method, path, **kwargs):
    return requests.request(
        method=method,
        url=f"https://dev-api-laas.wanted.co.kr{path}",
        headers={
            "project": "WANTED_DATA",
            "apiKey": WANTED_LAAS_API_KEY,
            "Content-Type": "application/json; charset=utf-8",
        },
        **kwargs,
    )


if __name__ == '__main__':
    WANTED_LAAS_API_KEY = get_parameter('/DATA/PIPELINE/API_KEY/OPENAI/DEV')

    doc_id = 88173997
    # res = call_wanted_api('GET', f"/api/document/channtest/{1}")
    collection_name = 'chann_test'
    body = {
        "dimension": 1536,
        "embedding_model": "text-embedding-ada-002",
        "service_type": "azure"
    }
    # res = call_wanted_api('POST', f'/api/collection/{collection_name}', json=body)
