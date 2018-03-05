from . import Reasoner

"""
is eligible if you are receiving paid
parental leave
is receiving acc weekly compensation
"""


class TestKey(Reasoner):
    key = 'isWorkingForFamiliesInWorkTaxCredit'


class TestWFF_InWorkTaxCreditDefault(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit (default state):
    Default benefit.isWorkingForFamiliesInWorkTaxCredit is FORBIDDEN
    Overriden by:
    Benefit: Working for Families - In Work Tax Credit (eligibility)
    """

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFFInWorkTaxCreditSingle(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit (eligibility):
    If applicant.isParent
    and not applicant.receivesIncomeTestedBenefit
    and applicant.isPrincipalCarer
    and income.ofApplicantAndSpouse > 0
    and applicant.relationshipStatus = "single"
    and applicant.worksWeeklyHours > 20
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
            "isNZResident": True,
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "relationshipStatus": "single",
            "worksWeeklyHours": 21
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "WorkingForFamiliesInWorkTaxCredit": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


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
            "isNZResident": True,
            "relationshipStatus": "complicated",
            "isParent": True,
            "isPrincipalCarer": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "child": {
            "isDependent": True
        },
        "couple": {
            "worksWeeklyHours": 30,
        },
        "threshold": {
            "income": {
                "WorkingForFamiliesInWorkTaxCredit": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
