#!usr/bin/env python
# -*- coding: utf-8 -*-

from . import Reasoner


class OrphansTests(Reasoner):
    key = 'isOrphansBenefit'


class TestOrphansBenefitForbiddenByDefault(OrphansTests):

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

    """
    Benefit: Part 1C Orphans' Benefit (eligibility in legislation):
    If child.isDependent and parents.areDeceasedMissingOrIncapable
    and applicant.isPrincipalCarerForOneYearFromApplicationDate
    and 18 ≤ applicant.Age and not applicant.isParent
    and applicant.isNZResident and applicant.normallyLivesInNZ
    then benefit.isOrphansBenefit is PERMITTED
    """
    body = {
        "applicant": {
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 87,
            "isParent": False,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "child": {
            "isDependent": True
        },
        "parents": {
            "areDeceasedMissingOrIncapable": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)


class TestOrphansBenefitForCarer(OrphansTests):

    body = {
        "applicant": {
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 21,
            "isParent": False,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "child": {
            "isDependent": True
        },
        "parents": {
            "areDeceasedMissingOrIncapable": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)


class TestOrphansBenefitForChildForbidden(OrphansTests):

    body = {
        "applicant": {
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 17,
            "isParent": False,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "child": {
            "isDependent": True
        },
        "parents": {
            "areDeceasedMissingOrIncapable": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)
