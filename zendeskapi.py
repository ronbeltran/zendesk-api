import logging
import requests
import json

ZENDESK_URL = 'https://%s.zendesk.com/oauth/tokens'


class Zendesk(object):

    def __init__(self, client_id, client_secret, company, scope=None):
        """ Assumes the Client credentials grant type for now """
        if not client_id or not client_secret or not company:
            raise ValueError("Client Id, Client Secret and Company Name cannot be blank")
        if not scope:
            scope = ['read']
        self.scope = scope
        self.company = company.lower()
        self.client_id = client_id
        self.client_secret = client_secret

    def oauth_login(self):
        url = ZENDESK_URL % (self.company)
        headers = {
            'content-type': 'application/json'
        }
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': ','.join(self.scope),
        }
        resp = requests.post(url,
                             data=json.dumps(payload),
                             headers=headers)
        return resp.status_code, json.loads(resp.content)
