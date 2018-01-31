from . import Reasoner


class TestWFFParentalTaxCredit(Reasoner):

    """
    Benefit: Working for Families
    - Parental Tax Credit (default state):
        Default benefit.isWorkingForFamiliesParentalTaxCredit is FORBIDDEN
        Overriden by: Benefit: Working for Families
        - Parental Tax Credit (eligibility)
    """

    key = 'isWorkingForFamiliesParentalTaxCredit'

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFParentalTaxCreditEligibility(Reasoner):

    """
        Benefit: Working for Families - Parental Tax Credit (eligibility):
        If 33 ≤ applicant.isPrincipalCarerForProportion
            and not applicant.receivesIncomeTestedBenefit
            and not applicant.hasReceivedPaidParentalLeavePayment
                then benefit.isWorkingForFamiliesParentalTaxCredit is PERMITTED
    """

    key = 'isWorkingForFamiliesParentalTaxCredit'

    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 33,
            "receivesIncomeTestedBenefit": False,
            "hasReceivedPaidParentalLeavePayment": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)


class TestWFFParentalTaxCreditEligUnsupportedChildsBenefit(Reasoner):

    """
        Benefit: Working for Families - Parental Tax Credit
        A. Forbidden if Unsupported Childs Benefit:
        If benefit.isUnsupportedChildsBenefit is PERMITTED
            then benefit.isWorkingForFamiliesParentalTaxCredit is FORBIDDEN

        Benefit: Part 1C Unsupported Child's Benefit (eligible):
            If applicant.isPrincipalCarerForOneYearFromApplicationDate
                and parents.areUnableToProvideSufficientCare
                and 18 ≤ applicant.Age
                and not applicant.isParent
                and applicant.isNZResident
                and child.isDependent
                    then benefit.isUnsupportedChildsBenefit is PERMITTED
    """

    key = 'isWorkingForFamiliesParentalTaxCredit'

    body = {
        "applicant": {
            "Age": 18,
            "isParent": False,
            "isNZResident": False
        },
        "parents": {
            "areUnableToProvideSufficientCare": True
        },
        "child": {
            "isDependent": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFParentalTaxCreditEligOrphansBenefit(Reasoner):

    """
        Benefit: Working for Families - Parental Tax Credit
        B. Forbidden if Orphans Benefit:
            If benefit.isOrphansBenefit is PERMITTED
                then benefit.isWorkingForFamiliesParentalTaxCredit is FORBIDDEN

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

    key = 'isWorkingForFamiliesParentalTaxCredit'

    body = {
        "applicant": {
            "isPrincipalCarerForOneYearFromApplicationDate": True,
            "Age": 18,
            "isParent": False,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "child": {
            "isDependent": True,
        },
        "parents": {
            "areDeceasedMissingOrIncapableThroughDisability": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)
