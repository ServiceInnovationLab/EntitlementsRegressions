"""
Benefit: Part 1C Orphans' Benefit (eligibility in legislation):
If child.isDependent
    and parents.areDeceasedMissingOrIncapableThroughDisability
    and applicant.isPrincipalCarerForOneYearFromApplicationDate
    and 18 ≤ applicant.Age
    and not applicant.isParent
    and applicant.isNZResident
    and applicant.normallyLivesInNZ
then benefit.isOrphansBenefit is PERMITTED
"""
from . import Reasoner


class OrphansTests(Reasoner):
    key = 'isOrphansBenefit'


class TestOrphansBenefitForbiddenByDefault(OrphansTests):

    body = {
        "applicant": {
            "Age": 30,
            "normallyLivesInNZ": True,
            "isNZResident": True,
            "hasAccommodationCosts": True,
            "hasSocialHousing": False,
            "receivesAccommodationSupport": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)


class TestOrphansBenefitForGrandparent(OrphansTests):

    body = {
        "applicant": {
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 87,
            "isParent": False,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "child": {"isDependent": True},
        "parents": {"areDeceasedMissingOrIncapableThroughDisability": True},
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
