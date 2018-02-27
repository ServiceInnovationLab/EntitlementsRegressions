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

        self.assertTrue(self.is_permitted)


"""
Update from Raap
"""


class TestWFFMinimumFamilyTCSingle(TestKey):

    body = {
        "income": {
            "ofApplicant": 2000
        },
        "applicant": {
            "worksWeeklyHours": 20,
            "relationshipStatus": "single",
            "isSelfEmployed": False
        },
        "benefit": {
            "isStudentAllowance": False
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_permitted)


class TestWFFMinimumFamilyTCCouple(TestKey):

    body = {
        "income": {
            "ofApplicantandSpouse": 2000
        },
        "applicant": {
            "worksWeeklyHours": 32,
            "relationshipStatus": "",
            "isSelfEmployed": False
        },
        "benefit": {
            "isStudentAllowance": False
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_permitted)


class TestWFFMinimumFamilyTCSelfEmployed(TestKey):

    body = {
        "income": {
            "ofApplicant": 2000
        },
        "applicant": {
            "worksWeeklyHours": 20,
            "relationshipStatus": "single",
            "isSelfEmployed": True
        },
        "benefit": {
            "isStudentAllowance": False
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)
