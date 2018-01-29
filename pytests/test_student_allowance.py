from . import Reasoner
from pprint import pprint
"""
 If applicant.isNZResident
    and applicant.normallyLivesInNZ
    and applicant.Age ≤ 65
    and 18 ≤ applicant.Age
    and applicant.isStudyingFullTime
    and not applicant.receivesIncomeTestedBenefit
        then benefit.isStudentAllowance is PERMITTED
"""


class TestStudentAllowance(Reasoner):
    key = 'isStudentAllowance'

    body = {
        "applicant": {
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "Age": 65,
            "isStudyingFullTime": True,
            "receivesIncomeTestedBenefit": True
        }

    }

    def test_reasoning(self):
        pprint(self.subject)
        # self.assertTrue(self.is_conclusive)
        # self.assertTrue(self.is_permitted)
