import json
import os
import requests
import unittest

from dotenv import load_dotenv, find_dotenv
# Load config from .env
load_dotenv(find_dotenv())
TOKEN = os.environ.get('RAAP_TOKEN')
BASE_URL = 'https://nz.raap.d61.io/api/v0/domain/nz-entitlements-eligibility'


class Reasoner(unittest.TestCase):

    def runReason(self, body):
        url = '{base_url}/reasoning/reason?criteria=draft'.format(
            base_url=BASE_URL)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {token}'.format(token=TOKEN)}
        return requests.post(url, headers=headers, data=json.dumps(body))
