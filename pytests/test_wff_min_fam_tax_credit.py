from . import Reasoner

"""
Applicant IS eligible if:

- Income from applicant and spouse is  less than 23816
- You work at least 30 hours each week (for a couple),
- or 20 hours each week as a single parent


Applicant is NOT eligible if they are:

- are receiving a student allowance
- self-employed
"""


class TestKey(Reasoner):
    key = 'isWorkingForFamiliesMinimumFamilyTaxCredit'


class TestWFF_MinimumFamilyTaxCreditDefault(TestKey):

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFFMinimumFamilyTaxCreditSingle(TestKey):

    body = {
        "applicant": {
            "isNZResident": True,
            "isPrincipalCarer": True,
            "worksWeeklyHours": 20,
            "relationshipStatus": "single",
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "workingForFamiliesMinTaxCredit": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestWFFMinimumFamilyTaxCreditSingleNotEnoughHours(TestKey):

    body = {
        "applicant": {
            "isNZResident": True,
            "isPrincipalCarer": True,
            "worksWeeklyHours": 18,
            "relationshipStatus": "single",
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "workingForFamiliesMinTaxCredit": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFFMinimumFamilyTaxCreditCouple(TestKey):

    body = {
        "applicant": {
            "isNZResident": True,
            "isPrincipalCarer": True,
            "relationshipStatus": "complicated",
        },
        "couple": {
            "worksWeeklyHours": 31,
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "workingForFamiliesMinTaxCredit": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestWFFMinimumFamilyTaxCreditCoupleNotEnoughHours(TestKey):

    body = {
        "applicant": {
            "isNZResident": True,
            "isPrincipalCarer": True,
            "relationshipStatus": "complicated",
        },
        "couple": {
            "worksWeeklyHours": 20,
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "workingForFamiliesMinTaxCredit": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFFMinimumFamilyTaxCreditOrphans(TestKey):
    """
    Applicant is eligible for Orphans benefit
    so conclude that instead of WFF FTC
    """
    body = {
        "applicant": {
            "isNZResident": True,
            "isPrincipalCarer": True,
            "Age": 21,
            "isNZResident": True,
            "isParent": False,
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "normallyLivesInNZ": True,
            "relationshipStatus": "single",
            "worksWeeklyHours": 20,
        },
        "threshold": {
            "income": {
                "workingForFamiliesMinTaxCredit": True
            }
        },
        "child": {
            "isDependent": True
        },
        "parents": {
            "areDeceasedMissingOrIncapable": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)

    def test_forbidden_orphans(self):
        self.assertTrue(self.isPermitted('isOrphansBenefit'))


class TestWFFMinimumFamilyTaxCreditUnsupportedChild(TestKey):
    """
    Applicant is eligible for Unsupported Child's benefit
    so conclude that instead of WFF FTC
    """
    body = {
        "applicant": {
            "Age": 19,
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "isParent": False,
            "isPrincipalCarer": True,
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "relationshipStatus": "single",
            "worksWeeklyHours": 20,
        },
        "threshold": {
            "income": {
                "workingForFamiliesMinTaxCredit": True
            }
        },
        "parents": {
            "areUnableToProvideSufficientCare": True
        },
        "child": {
            "isDependent": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)

    def test_forbidden_unsupported_child(self):
        self.assertTrue(self.isPermitted('isUnsupportedChildsBenefit'))
