from . import Reasoner


class TestWFFTaxCreditKey(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'


class TestWFFTaxCreditDefault(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (default state):
    Default benefit.isWorkingForFamiliesFamilyTaxCredit is FORBIDDEN
    Overriden by: Benefit: Working for Families
     - Family Tax Credit (eligibility)
    """

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFTaxCredit(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (eligibility):
        If applicant.isParent
            and 20 ≤ applicant.worksWeeklyHours
            and not applicant.receivesIncomeTestedBenefit
            and not benefit.isStudentAllowance
            and applicant.isPrincipalCarer
            and not benefit.isOrphansBenefit
                then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
    """

    body = {
        "applicant": {
            "isParent": True,
            "worksWeeklyHours": 20,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "isPrincipalCarerForOneYearFromApplicationDate": False,
            "Age": 16,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "benefit": {
            "isStudentAllowance": False,
            "isOrphansBenefit": False
        },
        "parents": {
            "areDeceasedMissingOrIncapableThroughDisability": False
        },
        "child": {
            "isDependent": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)


class TestWFFTaxCreditStudentAllowance(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (eligibility):
        If applicant.isParent
            and 20 ≤ applicant.worksWeeklyHours
            and not applicant.receivesIncomeTestedBenefit
            and not benefit.isStudentAllowance
            and applicant.isPrincipalCarer
            and not benefit.isOrphansBenefit
                then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
    """

    body = {
        "applicant": {
            "isParent": True,
            "worksWeeklyHours": 37,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "isStudyingFullTime": True,
            "Age": 65,
            "normallyLivesInNZ": True,
            "isNZResident": True,
            "receivesIncomeTestedBenefit": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFTaxCreditOrphans(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (eligibility):
        If applicant.isParent
            and 20 ≤ applicant.worksWeeklyHours
            and not applicant.receivesIncomeTestedBenefit
            and not benefit.isStudentAllowance
            and applicant.isPrincipalCarer
            and not benefit.isOrphansBenefit
                then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
    """

    body = {
        "applicant": {
            "isParent": False,
            "worksWeeklyHours": 37,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 18,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "child": {
            "isDependent": True
        },
        "parents": {
            "areDeceasedMissingOrIncapableThroughDisability": True
        }

    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)
