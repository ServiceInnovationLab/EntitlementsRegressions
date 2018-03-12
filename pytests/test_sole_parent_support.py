from . import Reasoner
from pprint import pprint


class TestSoleParentSupportNotSupported(Reasoner):
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
    key = 'isSoleParentSupport'

    body = {
        "applicant": {
            "isParent": True,
            "isInadequatelySupportedByPartner": True,
            "isMaintainingChild": True,
            "isNZResident": True,
            "Age": 20,
            "normallyLivesInNZ": True,
            "hasLivedInNZfor2Years": True
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
        self.assertTrue(self.is_permitted)


class TestSoleParentSupportSingle(Reasoner):
    """
    If applicant.relationshipStatus = "single"
        and applicant.isParent
        and applicant.isMaintainingChild
        and applicant.isNZResident
        and applicant.normallyLivesInNZ
        and 20 ≤ applicant.Age
        and child.Age < 14
        and child.isDependent
        and threshold.income.SoleParentSupport
        and applicant.normallyLivesInNZ
        and applicant.hasLivedInNZfor2Years
    then benefit.isSoleParentSupport is PERMITTED
    """
    key = 'isSoleParentSupport'

    body = {
        "applicant": {
            "isParent": True,
            "relationshipStatus": "single",
            "isMaintainingChild": True,
            "isNZResident": True,
            "Age": 20,
            "normallyLivesInNZ": True,
            "hasLivedInNZfor2Years": True
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
        self.assertTrue(self.is_permitted)
