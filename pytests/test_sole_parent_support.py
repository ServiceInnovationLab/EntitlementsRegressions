from . import Reasoner
from pprint import pprint
"""
Benefit: Part 1B Sole Parent Support (eligibility in legislation):
    If applicant.isParent
        and applicant.isInadequatelySupportedByPartner
        and applicant.isMaintainingChild
        and applicant.isNZResident
        and 20 ≤ applicant.Age
        and child.Age < 14
        and child.isDependent
        and threshold.income.SoleParentSupport
    then benefit.isSoleParentSupport is PERMITTED
"""


class TestSoleParentSupport(Reasoner):
    key = 'isSoleParentSupport'

    body = {
        "applicant": {
            "isParent": True,
            "isInadequatelySupportedByPartner": True,
            "isMaintainingChild": True,
            "isNZResident": True,
            "Age": 20
        },
        "child": {
            "isDependent": True,
            "Age": 5
        },
        "income": {
            "ofApplicantAndSpouse": 200,
            "fromMaintenancePayments": 200
        },
        "threshold": {
            "income": {
                "SoleParentSupport": True
            }
        }

    }

    def test_reasoning(self):
        pprint(self.subject)
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
