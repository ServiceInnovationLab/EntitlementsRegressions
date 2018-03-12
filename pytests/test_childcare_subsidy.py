from . import Reasoner


"""
Benefit: Childcare subsidy:Default benefit.isChildCareSubsidy is FORBIDDEN
Overriden by:
Benefit: Childcare subsidy (eligibility for disabled under 6s),
Benefit: Childcare subsidy (eligibility for under 5s)
"""


class TestChildSubsidyDefault(Reasoner):
    key = 'isChildCareSubsidy'

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


"""
Benefit: Childcare subsidy (eligibility for disabled under 6s):
If child.Age < 6
    and benefit.ChildDisabilityAllowance
    and applicant.isPrincipalCarer
    and threshold.income.ChildCareSubsidy
    and applicant.isNZResident
    and 3 ≤ child.WeeklyECEHours
    and 1 ≤ applicant.numberOfChildren
then benefit.isChildCareSubsidy is PERMITTED
"""


class ChildCareSubsidyDisabledUnder6s(Reasoner):

    key = 'isChildCareSubsidy'

    body = {
        "child": {
            "Age": 5,
            "hasMedicalCertification": True,
            "hasSeriousDisability": True,
            "isDependent": True,
            "requiresConstantCareAndAttention": True,
            "WeeklyECEHours": 4,
        },
        "applicant": {
            "numberOfChildren": 3,
            "isNZResident": True,
            "isPrincipalCarer": True,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "threshold": {
            "income": {
                "ChildCareSubsidy": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)

    def test_disability(self):
        self.assertTrue(self.isPermitted('ChildDisabilityAllowance'))


class ChildCareSubsidyDisabledExampleForJen(Reasoner):
    key = 'isChildCareSubsidy'
    body = {
        "applicant": {
            "Age": 24,
            "gaveBirthToThisChild": True,
            "hasAccommodationCosts": False,
            "hasSeriousDisability": False,
            "holdsCommunityServicesCard": False,
            "isNZResident": True,
            "isPrincipalCarer": True,
            "normallyLivesInNZ": True,
            "numberOfChildren": 1,
            "receivesIncomeTestedBenefit": False,
            "relationshipStatus": "single",
            "hasLivedInNZfor2Years": True,
            "isMaintainingChild": True,
            "hasMedicalCertificate": True,
            "hasReceivedPaidParentalLeavePayment": False,
            "isParent": True,
            "isPrincipalCarerForProportion": 100,
            "isStudyingFullTime": False,
            "employmentStatus": "notfulltime"
        },
        "child": {
            "hasSeriousDisability": True,
            "requiresConstantCareAndAttention": True,
            "WeeklyECEHours": 10, "isDependent": True,
            "Age": 5, "hasMedicalCertification": True
        },
        "children": {
            "dependentsUnder14": 1
        },
        "threshold": {
            "income": {
                "ChildCareSubsidy": True,
                "JobSeekerSupport": True,
                "SoleParentSupport": True,
                "AccommodationSupplement": True,
                "workingForFamiliesMinTaxCredit": True,
                "WorkingForFamiliesInWorkTaxCredit": True,
                "WorkingForFamiliesFamilyTaxCredit": True,
                "workingForFamiliesParentalTaxCredit": True,
                "SupportedLivingPayment": True, "YoungParentPayment": True
            },
            "isCommunityServicesCard": True,
            "cash": {
                "AccommodationSupplement": True, "HomeHelp": True
            }
        },
        "recipient": {
            "prepareForEmployment": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)

    def test_disability(self):
        self.assertTrue(self.isPermitted('ChildDisabilityAllowance'))


"""
Benefit: Childcare subsidy (eligibility for under 5s):
If child.Age < 5
    and applicant.isPrincipalCarer
    and threshold.income.ChildCareSubsidy
    and applicant.isNZResident
    and 3 ≤ child.WeeklyECEHours
    and 1 ≤ applicant.numberOfChildren
then benefit.isChildCareSubsidy is PERMITTED
"""


class ChildCareSubsidyUnder5s(Reasoner):

    key = 'isChildCareSubsidy'

    body = {
        "child": {
            "Age": 4,
            "WeeklyECEHours": 4
        },
        "applicant": {
            "numberOfChildren": 3,
            "isNZResident": True,
            "isPrincipalCarer": True
        },
        "threshold": {
            "income": {
                "ChildCareSubsidy": True
            }
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_permitted)
