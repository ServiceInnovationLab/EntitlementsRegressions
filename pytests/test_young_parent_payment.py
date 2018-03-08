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
        and threshold.income.YoungParentPayment
    then benefit.isYoungParentPayment is PERMITTED
"""


class TestYoungParentPayment(Reasoner):
    key = 'isYoungParentPayment'

    body = {
        "applicant": {
            "Age": 16,
            "isNZResident": True,
            "isPrincipalCarer": True,
            "normallyLivesInNZ": True,
            "isParent": True,
            "numberOfChildren": 1
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "YoungParentPayment": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


class TestYoungParentPaymentJenRetyped(Reasoner):
    key = 'isYoungParentPayment'
    body = {
        "applicant": {
            "Age": 17,
            "gaveBirthToThisChild": True,
            "hasAccommodationCosts": False,
            "hasLivedInNZfor2Years": True,
            "hasMedicalCertificate": True,
            "hasReceivedPaidParentalLeavePayment": False,
            "hasSeriousDisability": False,
            "holdsCommunityServicesCard": False,
            "isMaintainingChild": True,
            "isNZResident": True,
            "isParent": True,
            "isPrincipalCarer": True,
            "normallyLivesInNZ": True,
            "numberOfChildren": 1,
            "receivesIncomeTestedBenefit": False,
            "relationshipStatus": "single",
        },
        "child": {
            "hasSeriousDisability": False,
            "isDependent": True,
            "Age": 0,
            "hasMedicalCertification": True,
            "isDependent": True
        },
        "children": {
            "dependentsUnder14": 1
        },
        "threshold": {
            "income": {
                "AccommodationSupplement": True,
                "ChildCareSubsidy": True,
                "JobSeekerSupport": True,
                "SoleParentSupport": True,
                "SupportedLivingPayment": True,
                "WorkingForFamiliesFamilyTaxCredit": True,
                "WorkingForFamiliesInWorkTaxCredit": True,
                "workingForFamiliesMinTaxCredit": True,
                "workingForFamiliesParentalTaxCredit": True,
                "YoungParentPayment": True
            },
            "isCommunityServicesCard": True,
            "cash": {
                "AccommodationSupplement": True,
                "HomeHelp": True
            }
        },
        "recipient": {
            "prepareForEmployment": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
