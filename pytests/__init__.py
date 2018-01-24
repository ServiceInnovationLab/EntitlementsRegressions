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

    def setUp(self):
        self.runReason()

    @property
    def subject(self):
        return self.response.get('benefit').get(self.key)

    def findConclusiveReasoningResult(self):
        for rule in self.subject:
            if rule.get('reasoningResult') == 'CONCLUSIVE':
                return rule

    @property
    def is_conclusive(self):
        """Look for at least one conclusive reasoning result"""
        return (self.findConclusiveReasoningResult() is not None)

    @property
    def is_permitted(self):
        return (self.findConclusiveReasoningResult().get('goal')
                == self._expected_goal_response(modality='PERMITTED'))

    @property
    def is_forbidden(self):
        return (self.findConclusiveReasoningResult().get('goal')
                == self._expected_goal_response(modality='FORBIDDEN'))

    def _expected_goal_response(self, modality):
        return {
            "modality": modality,
            "negated": False,
            "value": True,
            "id": "benefit.{key}".format(key=self.key),
            "type": "BOOL"
        }

    def runReason(self):
        """Run reasoning on the server"""
        url = '{base_url}/reasoning/reason?criteria=draft'.format(
            base_url=BASE_URL)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {token}'.format(token=TOKEN)}
        self.response = requests.post(
            url, headers=headers, data=json.dumps(self.body)).json()
