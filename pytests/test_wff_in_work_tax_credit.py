from . import Reasoner

"""
is eligible if you are receiving paid
parental leave
is receiving acc weekly compensation
"""

class TestKey(Reasoner):
    key = 'isWorkingForFamiliesInWorkTaxCredit'


class TestWFFInWorkTaxCreditDefault(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit (default state):
    Default benefit.isWorkingForFamiliesInWorkTaxCredit is FORBIDDEN
    Overriden by:
    Benefit: Working for Families - In Work Tax Credit (eligibility)
    """

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFInWorkTaxCreditSingle(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit (eligibility):
    If applicant.isParent
    and not applicant.receivesIncomeTestedBenefit
    and applicant.isPrincipalCarer
    and income.ofApplicantAndSpouse > 0
    and applicant.relationshipStatus = "single"
    and applicant.worksWeeklyHours > 20
    and not benefit.isStudentAllowance
    and not benefit.isChildrensPension
    then benefit.isWorkingForFamiliesInWorkTaxCredit is PERMITTED

    You can't get in-work tax credit if you receive:
    - an income-tested benefit
    - a student allowance

    Overridden by: Benefit: Working for Families - In Work Tax Credit
    B. (eligibility work requirements for couples),
    Benefit: Working for Families - In Work Tax Credit
    A. (eligibility work requirements for singles),
    Benefit: Working for Families - In Work Tax Credit
    C. Forbidden if Student Allowance ,
    Benefit: Working for Families - In Work Tax Credit
    D. Forbidden is receiving "Parental Tax Credit"
    """

    body = {
        "applicant": {
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "relationshipStatus": "single",
            "weeklyHours": 21
        },
        "income": {
            "ofApplicantAndSpouse": 2
        },
        "benefit": {
            "isStudentAllowance": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)


class TestWFFInWorkTaxCreditForCouples(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit
    B. (eligibility work requirements for couples):
        If applicant.relationshipStatus ≠ "single"
            and applicant.worksWeeklyHours > 30
                then benefit.isWorkingForFamiliesInWorkTaxCredit is PERMITTED
    """

    body = {
        "applicant": {
            "relationshipStatus": "",
            "worksWeeklyHours": 30,
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "income": {
            "ofApplicantAndSpouse": 2
        },
        "benefit": {
            "isStudentAllowance": False,
            "isChildrensPension": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)
