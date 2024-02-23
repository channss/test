import boto3
import requests

def get_parameter(key):
    ssm = boto3.client('ssm', region_name='ap-northeast-2')
    return ssm.get_parameter(Name=key, WithDecryption=True)['Parameter']['Value']

# class Env(StageABC):
#     _stage = {
#         'nextweek': 'nw',
#         'www': 'www',
#     }
#     base_url = {
#         'nextweek': 'https://nextweek-api-laas.wanted.co.kr',
#         'www': 'https://api-laas.wanted.co.kr',
#     }


def call_wanted_api(method, path, **kwargs):
    return requests.request(
        method=method,
        # url=f"{Env.config('base_url')}{path}",
        url=f"https://nextweek-api-laas.wanted.co.kr{path}",
        headers={
            "project": "WANTED_DATA",
            "apiKey": WANTED_LAAS_API_KEY,
            "Content-Type": "application/json; charset=utf-8",
        },
        **kwargs,
    )

if __name__ == '__main__':
    WANTED_LAAS_API_KEY = get_parameter('/DATA/PIPELINE/API_KEY/OPENAI')

    doc_id = 88173997
    res = call_wanted_api('GET', f"/api/document/wanted_data_catalog/{doc_id}")