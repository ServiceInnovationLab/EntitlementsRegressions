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


class TestWorkingForFamiliesFamilyTaxCreditStudentAllowanceForbidden(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'

    body = {
        "applicant": {
            "isParent": True,
            "worksWeeklyHours": 37,
            "receivesIncomeTestedBenefit": False,
            "isPrincipalCarer": True,
            "isStudyingFullTime": True,
            "Age": 65,
            "normallyLivesInNZ": True,
            "isNZResident": True,
            "receivesIncomeTestedBenefit": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)
