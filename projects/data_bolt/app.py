import re
import json
import logging
from threading import Thread

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from slack_sdk.errors import SlackApiError
from melting_pot.aws import SSMOperator

ssm = SSMOperator()
bot_token = ssm.get_parameter('/DATA/SLACK/OAUTH/TOKEN', with_decryption=True)
app_token = ssm.get_parameter('/DATA/SLACK/SOCKET/TOKEN', with_decryption=True)
service_dict = json.loads(ssm.get_parameter(f'/DATA/WWW/GOOGLE/SERVICE_CREDENTIALS', with_decryption=True))

logging.basicConfig(level=logging.ERROR)  # Set logging level to WARNING

# Initializes your app with your bot token and socket mode handler
app = App(token=bot_token)


def findings_replace_slack_user_name(text, client):
    """
    Slack user, user-group, channel 등 mention을 변환하는 정규식입니다.
    Slack mention은 '<' 와 '>' 사이에 들어옵니다. 
    그리고 종류에 따라 @, !, #, | 등의 character가 붙습니다.
    """
    pattern = r'<[@|!#]([^>]+)>'
    def replace(match):
        user_id = match.group(1)
        try:
            user = client.users_info(user=user_id).get('user')
            return user['profile']['real_name']
        except SlackApiError:
            return user_id
    replaced_text = re.sub(pattern, replace, text)
    return replaced_text


def build_gpt_error_slack_blocks(title, response):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f'{title}'
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f'글자 수가 너무 많거나, Wanted LaaS 서버에 일시 오류가 있을 수 있습니다. \nError Message: ```{response}```',
                },
            ]
        }
    ],


def laas_findings_confluence_thread(event, client, say):
    print(event)
    from projects.data_bolt.middleware import findings_title_generator, findings_content_generator, FindingsCreator

    item_channel = event['item']['channel']
    item_ts = event['item']['ts']
    item_user = event['item_user']
    reaction_user = event['user']

    # SKIP if item_user is Bolt: 주 1회 요약된 findings를 볼트가 작성하기 때문에, 볼트가 쓴 글은 처리할 필요 없음
    if item_user == 'U029GCLFNG6':
        return

    # SKIP if emoji already added: 여러번 요약될 가능성 차단.
    reactions = client.reactions_get(
        channel=item_channel,
        timestamp=item_ts,
    )
    findings_emoji_count = sum(d['count'] for d in reactions['message']['reactions'] if d['name'] == '파인딩스2')
    if findings_emoji_count > 1:
        return

    # Retrieve the text content of the post using the Slack API
    conversation = client.conversations_replies(
        channel=item_channel,
        ts=item_ts,
    )
    message = conversation['messages'][0]
    # print(message)
    text = findings_replace_slack_user_name(message['text'], client)
    print(text)
    slack_link = f'https://wantedx.slack.com/archives/{item_channel}/p{message["ts"].replace(".", "")}'
    if message.get('thread_ts'): slack_link += f'?thread_ts={message["thread_ts"]}'

    try:
        # generate title
        res_title = findings_title_generator(text).json()
        title = res_title['choices'][0]['message']['content']
        print(title)
    except KeyError as e:
        say(
            channel=event['user'],
            blocks=build_gpt_error_slack_blocks('findings 제목 생성에 실패했습니다', res_title)
        )
        raise e

    try:
        # generate content
        res_content = findings_content_generator(text).json()
        content = res_content['choices'][0]['message']['content']
        content += f'\n\nSlack Link: <a href="{slack_link}">{slack_link}</a>'
        print(content)
    except KeyError as e:
        say(
            channel=event['user'],
            blocks=build_gpt_error_slack_blocks('findings 내용 요약에 실패했습니다', res_content)
        )
        raise e

    confluence = FindingsCreator()
    try:
        page_info = confluence.client.create_page(confluence.space, title, str(content), parent_id=confluence.parent)
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f'ㅍㅇㄷㅅ Confluence 문서가 생성되었습니다.'
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'<{page_info["_links"]["base"] + page_info["_links"]["webui"]}|Link to Confluence Page>'
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f'*Title*: {title}',
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",

                        "text": f'*Editor*: <@{item_user}>',
                    },
                    {
                        "type": "mrkdwn",
                        "text": f'*Uploader*: <@{reaction_user}>',
                    }
                ]
            },
        ]
        # say(
        #     channel=item_channel,
        #     blocks=blocks,
        #     thread_ts=item_ts,
        # )
    except Exception as e:
        say(
            channel=event['user'],
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "페이지 생성에 실패했습니다."
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f'Error Message: ```{e}```',
                        },
                    ]
                }
            ]
        )
        raise e


@app.event("reaction_added")
def reaction(event, client, say):
    """
    이모지에 따라 트리거되는 작업을 정의합니다.
    """
    match event['reaction']:
        case 'microsoft':
            t = Thread(target=laas_findings_confluence_thread, args=(event, client, say))
            t.start()


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()