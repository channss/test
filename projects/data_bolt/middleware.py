from projects.data_bolt import call_wanted_api, ATLASSIAN_API_KEY


def findings_title_generator(content):
    return call_wanted_api('POST', '/api/preset/chat/completions', json={
        "hash": "4260f7c5f78ebe0e7d3149a0c372eb2c0118744038db46b643e2883642d7aee1",
        "params": {"paragraph": content},
    })


def findings_content_generator(content):
    return call_wanted_api('POST', '/api/preset/chat/completions', json={
        "hash": "5dea49a99e75c0b1d0120fa8f99b852d3071b80e8deecc1fb5e6b02e767663cd",
        "params": {"paragraph": content},
    })


class FindingsCreator:
    parent = 2997158109
    space = 'DATA'

    def __init__(self):
        from atlassian import Confluence
        self.base_url = 'https://wantedlab.atlassian.net'
        self.client = Confluence(
            url=self.base_url,
            username='jongwon@wantedlab.com',
            password=ATLASSIAN_API_KEY,
        )

    def get_child_page_list(self, id):
        pages = self.client.get_page_child_by_type(page_id=id, type='page')
        return [{"id": page['id'], "title": page['title']} for page in pages]
