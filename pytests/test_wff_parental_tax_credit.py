from . import Reasoner

class TestKey(Reasoner):
    key = 'isWorkingForFamiliesParentalTaxCredit'


"""
Working for Families Parental Tax Credits

Applicant IS eligible if:

- they are the principal carer for a proportion of 33% or greater

Applicant is NOT eligible if they:

- are receiving an income tested benefit
- are receiving paid parent leave
- are receiving unsupported childs benefit
- receiving orphans benefit
- are receiving a student allowance
"""


class TestWFFParentalTaxCredit(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 34,
            "receivesIncomeTestedBenefit": False
        },
        "benefit": {
            "isPaidParentalLeave": False,
            "isStudentAllowance": False,
            "isOrphansBenefit": False,
            "isUnsupportedChildsBenefit": False,
            "isOnACCCompensation": False
        }

    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)
