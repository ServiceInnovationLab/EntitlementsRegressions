from . import Reasoner

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


class TestWorkingForFamiliesFamilyTaxCreditOrphansForbidden(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'

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
