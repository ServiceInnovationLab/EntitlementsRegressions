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
    and (income.ofApplicantAndSpouse + income.fromMaintenancePayments) < 628
        then benefit.isSoleParentSupport is PERMITTED

"""


class TestSoleParentSupport(Reasoner):
    key = 'isSoleParentSupport'

    body = {
        "applicant": {
            "normallyLivesInNZ": True,
            "isNZResident": True,
            "isParent": True,
            "isMaintainingChild": True,
            "isUnableToSupportThemselves": True
        },
        "child": {
            "isDependent": True
        }

    }

    def test_reasoning(self):
        pprint(self.subject)
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
