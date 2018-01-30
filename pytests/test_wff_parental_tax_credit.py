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
                then benefit.isWorkingForFamiliesParentalTaxCreditis PERMITTED
            Overriden by: Benefit: Working for Families - Parental Tax Credit
            A. Forbidden if Unsupported Childs Benefit,
                Benefit: Working for Families - Parental Tax Credit
            B. Forbidden if Orphans Benefit
    """

    key = 'isWorkingForFamiliesParentalTaxCredit'

    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 33,
            "receivesIncomeTestedBenefit": False,
            "hasReceivedPaidParentalLeavePayment": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)


class TestWFFParentalTaxCreditUnsupChildsBene(Reasoner):

    """
        Benefit: Working for Families - Parental Tax Credit (eligibility):
        If 33 ≤ applicant.isPrincipalCarerForProportion
            and not applicant.receivesIncomeTestedBenefit
            and not applicant.hasReceivedPaidParentalLeavePayment
                then benefit.isWorkingForFamiliesParentalTaxCredit is PERMITTED
            Overriden by: Benefit: Working for Families - Parental Tax Credit
                A. Forbidden if Unsupported Childs Benefit,
                    Benefit: Working for Families - Parental Tax Credit
                B. Forbidden if Orphans Benefit
    """

    key = 'isWorkingForFamiliesParentalTaxCredit'

    body = {
        "applicant": {
            "isPrincipalCarerForProportion": 33,
            "receivesIncomeTestedBenefit": False,
            "hasReceivedPaidParentalLeavePayment": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)
