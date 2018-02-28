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


class TestWFF_ParentalTaxCreditDefault(TestKey):
    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFF_ParentalTaxCredit(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 34,
            "receivesIncomeTestedBenefit": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestWFF_ParentalLessChildcare(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 4,
            "receivesIncomeTestedBenefit": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFF_ParentalTaxCreditOnMTBenefit(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 100,
            "receivesIncomeTestedBenefit": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFF_ParentalTaxCreditForbiddenOnAcc(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 34,
            "receivesIncomeTestedBenefit": False,
            "isOnACCCompensation": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFF_ParentalTaxCreditForbiddenOrphans(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 34,
            "receivesIncomeTestedBenefit": False,
            # add the orphans bene requirements
            "Age": 87,
            "isNZResident": True,
            "isParent": False,
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "normallyLivesInNZ": True
        },
        "child": {
            "isDependent": True
        },
        "parents": {
            "areDeceasedMissingOrIncapable": True
        }
    }

    def test_reasoning(self):
        # Orphans benefit is permitted, so WFF PTC is not
        self.assertTrue(self.isPermitted('isOrphansBenefit'))
        self.assertTrue(self.is_forbidden)


class TestWFF_ParentalTaxCreditForbiddenStudents(TestKey):
    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 34,
            "receivesIncomeTestedBenefit": False,
            # add the student allowance requirements
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "Age": 25,
            "isStudyingFullTime": True,
        }
    }

    def test_reasoning(self):
        # Orphans benefit is permitted, so WFF PTC is not
        self.assertTrue(self.isPermitted('isStudentAllowance'))
        self.assertTrue(self.is_forbidden)
