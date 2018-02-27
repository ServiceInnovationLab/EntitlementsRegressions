from . import Reasoner

"""
Benefit: Young Parent Payment (eligibility):
    If 16 ≤ applicant.Age
        and applicant.Age ≤ 19
        and child.isDependent
        and applicant.isNZResident
        and applicant.normallyLivesInNZ
        and applicant.isParent
        and not benefit.isOrphansBenefit
        and not benefit.isUnsupportedChildsBenefit
        and 1 ≤ applicant.numberOfChildren
        and threshold.income.PaidParentalLeave
    then benefit.isPaidParentalLeave is PERMITTED
"""


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
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestPaidParentalNotEmployed(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveEmployedRequirements": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalSelfEmployed(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveSelfEmploymentRequirements": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestPaidParentalTransferredToSpouse(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveSelfEmploymentRequirements": True
        },
        "spouse": {
            "transferringEntitlementToApplicant": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveRequirements": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestPaidParentalTransferredToSpouseNotEligible(TestPaidParentalLeave):
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveSelfEmploymentRequirements": True
        },
        "spouse": {
            "transferringEntitlementToApplicant": True,
            "gaveBirthToThisChild": True,
            "meetsPaidParentalLeaveRequirements": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestPaidParentalNotSpouse(TestPaidParentalLeave):
    """Auntie or grandma, or the father who is not the spouse"""
    body = {
        "applicant": {
            "isStoppingWorkToCareForChild": True,
            "gaveBirthToThisChild": False,
            "meetsPaidParentalLeaveSelfEmploymentRequirements": True
        },
        "spouse": {
            "gaveBirthToThisChild": False,
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
