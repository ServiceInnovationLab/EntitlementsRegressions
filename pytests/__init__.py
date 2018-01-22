import json
import os
import requests
import unittest
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

from dotenv import load_dotenv, find_dotenv
# Load config from .env
load_dotenv(find_dotenv())
TOKEN = os.environ.get('RAAP_TOKEN')

class Reasoner(unittest.TestCase):
    def runReason(self, body):
        url = 'https://nz.raap.d61.io/api/v0/domain/nz-entitlements-eligibility/reasoning/reason?criteria=draft'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {token}'.format(token=TOKEN)}
        return requests.post(url, headers=headers, data=json.dumps(body))