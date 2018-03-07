from . import Reasoner


class TestPaidParentalLeave(Reasoner):
    key = 'isPaidParentalLeave'


class TestPaidParentalLeaveDefault(TestPaidParentalLeave):
    body = {}

    def test_default(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalLeaveEligible(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestPaidParentalLeaveAdoptedEligible(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "child": {
            "Age": 1,
            "AdoptedByApplicant": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestPaidParentalLeaveAdoptedNotStoppingWork(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": False,
            # "meetsPaidParentalLeaveEmployedRequirements": False
        },
        "child": {
            "Age": 1,
            "AdoptedByApplicant": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalLeaveAdoptedNotWorkingTenHours(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": False
        },
        "child": {
            "Age": 1,
            "AdoptedByApplicant": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalNotEmployed(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": False
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalTransferredToSpouse(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "spouse": {
            "transferringEntitlementToApplicant": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)

# Spouse of the person who gave birth,
# but the "mother" isn't eligible to transfer
# her entitlement


class TestPaidParentalTransferredToSpouseNotEligible(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "spouse": {
            "transferringEntitlementToApplicant": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": False
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalNotSpouse(TestPaidParentalLeave):
    """Auntie or Koro, or the father who is not the spouse"""
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "spouse": {
            "gaveBirthToThisChild": False,
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestPaidParentalNotSpouseNotMeetingWorkREq(TestPaidParentalLeave):
    """Auntie or Koro, or the father who is not the spouse"""
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveEmployedRequirements": False
        },
        "spouse": {
            "gaveBirthToThisChild": False,
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalNullWorkReq(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            # "meetsPaidParentalLeaveEmployedRequirements": False
        },
        "spouse": {
            "gaveBirthToThisChild": False,
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalNullStoppingWork(TestPaidParentalLeave):
    body = {
        "applicant": {
            # "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "spouse": {
            "gaveBirthToThisChild": False,
        },
        "child": {
            "Age": 0
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalNullChildAge(TestPaidParentalLeave):
    body = {
        "applicant": {
            # "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": True
        },
        "spouse": {
            "gaveBirthToThisChild": False,
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
