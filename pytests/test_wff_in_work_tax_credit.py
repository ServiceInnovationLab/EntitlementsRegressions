from . import Reasoner

"""
Benefit: Working for Families - In Work Tax Credit (eligibility):
    If applicant.isParent
        and not applicant.receivesIncomeTestedBenefit
        and applicant.isPrincipalCarer
        and income.ofApplicantAndSpouse < 1
            then benefit.isWorkingForFamiliesInWorkTaxCredit is PERMITTED

Overriden by:
    Benefit: Working for Families - In Work Tax Credit
        A. (eligibility work requirements for singles),
    Benefit: Working for Families - In Work Tax Credit
        B. (eligibility work requirements for couples),
    Benefit: Working for Families - In Work Tax Credit
        C. Forbidden if Student Allowance ,
    Benefit: Working for Families - In Work Tax Credit
        D. Forbidden is recieving "Parental Tax Credit"
"""


class TestWFFInWorkTaxCredit(Reasoner):

    key = 'isWorkingForFamiliesInWorkTaxCredit'

    body = {
        "applicant": {
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
        },
        "income": {
            "ofApplicantAndSpouse": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)
