from . import Reasoner


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


class TestWFFInWorkTaxCredit(TestKey):

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
            D. Forbidden is receiving "Parental Tax Credit"
    """

    body = {
        "applicant": {
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "income": {
            "ofApplicantAndSpouse": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)


class TestWFFInWorkTaxCreditForSingles(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit
    A. (eligibility work requirements for singles):
        If applicant.relationshipStatus = "single"
            and applicant.worksWeeklyHours < 20
                then benefit.isWorkingForFamiliesInWorkTaxCredit is FORBIDDEN
    """

    body = {
        "applicant": {
            "relationshipStatus": "single",
            "worksWeeklyHours": 19,
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "income": {
            "ofApplicantAndSpouse": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFInWorkTaxCreditForCouples(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit
    B. (eligibility work requirements for couples):
        If applicant.relationshipStatus ≠ "single"
            and applicant.worksWeeklyHours < 30
                then benefit.isWorkingForFamiliesInWorkTaxCredit is FORBIDDEN
    """

    body = {
        "applicant": {
            "relationshipStatus": "",
            "worksWeeklyHours": 29,
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "income": {
            "ofApplicantAndSpouse": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFInWorkTaxCreditStudentAllowance(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit
    C. Forbidden if Student Allowance:
        If benefit.isStudentAllowance is PERMITTED
            then benefit.isWorkingForFamiliesInWorkTaxCredit is FORBIDDEN
    """

    body = {
        "applicant": {
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "Age": 65,
            "isStudyingFullTime": True,
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "income": {
            "ofApplicantAndSpouse": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFInWorkTaxCreditParentalTaxCredit(TestKey):

    """
    Benefit: Working for Families - In Work Tax Credit
    D. Forbidden is receiving "Parental Tax Credit":
        If benefit.isWorkingForFamiliesParentalTaxCredit is PERMITTED
            then benefit.isWorkingForFamiliesInWorkTaxCredit is FORBIDDEN

    (These rules must be permitted for D. to pass
    applicant.isPrincipalCarerForProportion is a percentage)

    Benefit: Working for Families - Parental Tax Credit (eligibility):
        If 33 ≤ applicant.isPrincipalCarerForProportion
            and not applicant.receivesIncomeTestedBenefit
            and not applicant.hasReceivedPaidParentalLeavePayment
                then benefit.isWorkingForFamiliesParentalTaxCredit is PERMITTED
    """

    body = {
        "applicant": {
            "isParent": True,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "isPrincipalCarerForProportion": 33,
            "hasReceivedPaidParentalLeavePayment": False

        },
        "income": {
            "ofApplicantAndSpouse": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)
