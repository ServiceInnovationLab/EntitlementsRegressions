from . import Reasoner

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


class TestUnsupportedChildsBenefit(Reasoner):
    key = 'isUnsupportedChildsBenefit'

    body = {
        "applicant": {
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 19,
            "isParent": False,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "parents": {
            "areUnableToProvideSufficientCare": True
        },
        "child": {
            "isDependent": True
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_permitted)
