from . import Reasoner
"""
Benefit: Working for Families - Family Tax Credit (eligibility):
If applicant.isParent
    and 20 ≤ applicant.worksWeeklyHours
    and not applicant.receivesIncomeTestedBenefit
    and not benefit.isStudentAllowance
    and applicant.isPrincipalCarer
    and not benefit.isOrphansBenefit is PERMITTED
    and not benefit.isUnsupportedChildsBenefit is PERMITTED
        then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
"""


class TestWorkingForFamiliesFamilyTaxCredit(Reasoner):

    # TODO: Add enough info to cause
    # isOrphansBenefit isUnsupportedChildsBenefit
    # to not be permitted

    key = 'isWorkingForFamiliesFamilyTaxCredit'
    body = {
        "applicant": {
            "isParent": True,
            "worksWeeklyHours": 19,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True
        },
        "benefit": {
            "isStudentAllowance": False,
        },
        "threshold": {
            "income": {
                "AccommodationSupplement": True
            },
            "cash": {
                "AccommodationSupplement": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)


class TestWorkingForFamiliesFamilyTaxCreditNotEnoughInfo(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'
    body = {
        "applicant": {
            "Age": 30,
            "normallyLivesInNZ": True,
            "isNZResident": True,
            "hasAccommodationCosts": True,
            "hasSocialHousing": False,
            "receivesAccommodationSupport": False
        },
        "threshold": {
            "income": {
                "AccommodationSupplement": True
            }
        }
    }

    def testNotEnoughInfo(self):
        # print(self.subject)
        print(self.findConclusiveReasoningResult())
        self.assertFalse(self.is_conclusive)
