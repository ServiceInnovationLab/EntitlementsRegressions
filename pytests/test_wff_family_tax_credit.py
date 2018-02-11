from . import Reasoner


class TestWFFTaxCreditKey(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'


class TestWFFTaxCreditDefault(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (default state):
    Default benefit.isWorkingForFamiliesFamilyTaxCredit is FORBIDDEN
    Overriden by: Benefit: Working for Families
     - Family Tax Credit (eligibility)
    """


    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFTaxCredit(TestWFFTaxCreditKey):

    """
    If applicant.isParent
    and applicant.isPrincipalCarer
    then benefit.isWorkingForFamiliesFamilyTaxCredit
    is PERMITTED
    """

    body = {
        "applicant": {
            "isParent": True,
            "isPrincipalCarer": True
        },
        "benefit": {
            "isOrphansBenefit": False,
            "isUnsupportedChildsBenefit": False,
            "isFosterCareAllowance": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)


class TestWFFTaxCreditKey(Reasoner):

    key = 'isWorkingForFamiliesFamilyTaxCredit'


class TestWFFTaxCreditDefault(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (default state):
    Default benefit.isWorkingForFamiliesFamilyTaxCredit is FORBIDDEN
    Overriden by: Benefit: Working for Families
     - Family Tax Credit (eligibility)
    """

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFTaxCredit(TestWFFTaxCreditKey):

    """
    Benefit: Working for Families - Family Tax Credit (eligibility):
        If applicant.isParent
        and applicant.isPrincipalCarer
        and not benefit.isOrphansBenefit
        and not benefit.isUnsupportedChildsBenefit
        and not benefit.isFosterCareAllowance
        then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
    """

    body = {
        "applicant": {
            "isParent": True,
            "isPrincipalCarer": True
        },
        "benefit": {
            "isOrphansBenefit": False,
            "isUnsupportedChildsBenefit": False,
            "isFosterCareAllowance": False
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)
