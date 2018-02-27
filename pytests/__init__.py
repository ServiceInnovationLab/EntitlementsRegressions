import json
import os
import requests
import unittest
from pprint import pprint

from dotenv import load_dotenv, find_dotenv
# Load config from .env
load_dotenv(find_dotenv())
TOKEN = os.environ.get('RAAP_TOKEN')
BASE_URL = 'https://nz.raap.d61.io/api/v0/domain/nz-entitlements-eligibility'


class BenefitResult(object):
    def __init__(self, response, benefit):
        self.benefit = benefit
        self.response = response

    def find_conclusive_reasoning_result(self):
        benefit_result = self.response.get('benefit').get(self.benefit)
        if benefit_result is not None:
            for rule in benefit_result:
                if rule.get('reasoningResult') == 'CONCLUSIVE':
                    return rule.get('goal')

    def has_goal_response_modality(self, modality):
        expected = {
            "modality": modality,
            "negated": False,
            "value": True,
            "id": "benefit.{benefit}".format(benefit=self. benefit),
            "type": "BOOL"
        }
        goal = self.find_conclusive_reasoning_result()
        return goal == expected


class Reasoner(unittest.TestCase):

    def setUp(self):
        self.runReason()

    @property
    def is_permitted(self):
        """Is the main benefit permitted?"""
        return self.isPermitted(self.key)

    @property
    def is_forbidden(self):
        """Is the main benefit forbidden?"""
        return self.isForbidden(self.key)

    def isForbidden(self, benefit):
        return self.isResult(benefit=benefit, modality='FORBIDDEN')

    def isPermitted(self, benefit):
        return self.isResult(benefit=benefit, modality='PERMITTED')

    def isResult(self, benefit, modality):
        return BenefitResult(
            response=self.response,
            benefit=benefit
        ).has_goal_response_modality(
            modality=modality)

    def runReason(self):
        """Run reasoning on the server"""
        url = '{base_url}/reasoning/reason?criteria=draft'.format(
            base_url=BASE_URL)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {token}'.format(token=TOKEN)}
        response = requests.post(
            url, headers=headers, data=json.dumps(self.body))
        try:
            self.response = response.json()
        except:
            print(response.text)
            raise
