"""
Benefit: Part 1C Unsupported Child's Benefit (eligible):
If applicant.isPrincipalCarerForOneYearFromApplicationDate
    and parents.areUnableToProvideSufficientCare
    and 18 ≤ applicant.Age
    and not applicant.isParent
    and applicant.isNZResident
    and child.isDependent
then benefit.isUnsupportedChildsBenefit is PERMITTED
"""
from . import Reasoner

MIMIMUM_REQUIREMENTS = {
    "applicant": {
        "Age": 18,
        "isPrincipalCarerForOneYearFromApplicationDate": True,
        "isNZResident": True,
        "isParent": False,
        # "normallyLivesInNZ": True
    },
    "parents": {"areUnableToProvideSufficientCare": True},
    "child": {"isDependent": True}
}


class UnsupportedChildsTests(Reasoner):
    key = 'isUnsupportedChildsBenefit'


class TestUnsupportedChildsBenefitForbiddenByDefault(UnsupportedChildsTests):
    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)


class TestUnsupportedChildsBenefit(UnsupportedChildsTests):
    body = MIMIMUM_REQUIREMENTS

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
