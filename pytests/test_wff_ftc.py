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

Orphans Benefit should return FORBIDDEN
    If child.isDependent
        and parents.areDeceasedMissingOrIncapableThroughDisability
        and applicant.isPrincipalCarerForOneYearFromApplicationDate
        and 18 ≤ applicant.age
        and not applicant.isParent
        and applicant.isNZResident
        and applicant.normallyLivesInNZ
            then benefit.isOrphansBenefit is PERMITTED

isStudentAllowance should return FORBIDDEN
    If applicant.isNZResident
        and applicant.normallyLivesInNZ
        and applicant.age ≤ 65
        and 18 ≤ applicant.age
        and applicant.isStudyingFullTime
        and not applicant.receivesIncomeTestedBenefit
            then benefit.isStudentAllowance is PERMITTED
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
            "isStudyingFullTime": False
        },
        "benefit": {
            "isStudentAllowance": False,
            "isOrphansBenefit": False
        },
        "child": {
            "isDependent": False
        },
        "parents": {
            "areDeceasedMissingOrIncapableThroughDisability": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_conclusively_forbidden)
