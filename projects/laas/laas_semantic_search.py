import boto3
import requests
import hashlib
import json
from argparse import ArgumentParser

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


def semantic_search(skill, collection):
    return requests.request(
        method="POST",
        url=f"https://dev-api-laas.wanted.co.kr/api/document/{collection}/similar/text",
        headers={
            "project": "WANTED_DATA",
            "apiKey": WANTED_LAAS_API_KEY,
            "Content-Type": "application/json; charset=utf-8",
        },
        json={
            "text": skill,
            "limit": 5,
            "offset": 0,
            "with_metadata": True,
            "with_vector": False,
            "min_score": 0.8
        }
    )


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--keyword', required=True, type=str)
    args = parser.parse_args()

    WANTED_LAAS_API_KEY = get_parameter('/DATA/PIPELINE/API_KEY/OPENAI/DEV')

    collection_name = 'channtest'

    # skills = get_skills().to_dict(orient='records')
    # for s in skills:
    #     sname = s['content']
    #     doc_id = hashing(sname)
    #     response = call_wanted_api(
    #         'PUT',
    #         f'/api/document/{collection_name}/{doc_id}',
    #         json={
    #             'text': sname,
    #         },
    #     )
    #     print(doc_id, sname, response.text)
    # response = call_wanted_api('GET', f'/api/collection/{collection_name}')
    res = semantic_search(args.keyword, collection_name)
    print(json.loads(res.text))
