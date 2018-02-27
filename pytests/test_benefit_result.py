import unittest
from . import BenefitResult


class TestBenefitResult(unittest.TestCase):
    def test_finds_forbidden(self):
        response = {
            'applicant': {},
            'benefit': {
                'isChocolate': [
                    {
                        'dependencies': {'factsUsed': [], 'rulesUsed': []},
                        'goal': {
                            'id': 'benefit.isChocolate',
                            'type': 'BOOL',
                            'value': False
                        },
                        'reasoningResult': 'INCOMPLETE'
                    },
                    {
                        'dependencies': {
                            'factsUsed': [], 'rulesUsed': ['a', 'b']
                        },
                        'goal': {
                            'id': 'benefit.isChocolate',
                            'modality': 'FORBIDDEN',
                            'negated': False,
                            'type': 'BOOL',
                            'value': True
                        },
                        'reasoningResult': 'CONCLUSIVE'
                    },
                    {
                        'dependencies': {'factsUsed': [], 'rulesUsed': []},
                        'goal': {
                            'id': 'benefit.isChocolate',
                            'modality': 'PERMITTED',
                            'negated': False,
                            'type': 'BOOL',
                            'value': True
                        },
                        'reasoningResult': 'INCOMPLETE'
                    }
                ],
            },
            'child': {},
            'children': {},
            'couple': {},
            'parents': {},
            'spouse': {}
        }

        result = BenefitResult(
            response=response, benefit='isChocolate'
        ).has_goal_response_modality(
            modality='FORBIDDEN'
        )
        self.assertTrue(result)
