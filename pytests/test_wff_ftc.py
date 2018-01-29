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


class TestWorkingForFamiliesFamilyTaxCredit(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'

    body = {
        "applicant": {
            "isParent": True,
            "worksWeeklyHours": 20,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "isPrincipalCarerForOneYearFromApplicationDate": False,
            "Age": 16,
            "isNZResident": False,
            "normallyLivesInNZ": False
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
