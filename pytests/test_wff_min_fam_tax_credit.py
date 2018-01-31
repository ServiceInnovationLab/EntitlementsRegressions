from . import Reasoner


class TestKey(Reasoner):
    key = 'isWorkingForFamiliesMinimumFamilyTaxCredit'


class TestWFFMinFamTaxCreditDefault(TestKey):

    """
    Benefit: Working for Families - Minimum Family Tax Credit (default state):
    Default benefit.isWorkingForFamiliesMinimumFamilyTaxCredit is FORBIDDEN
    Overriden by: Benefit: Working for Families
     - Minimum Family Tax Credit (eligibility)
    """

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)
        self.assertTrue(self.is_conclusive)


class TestWFFMinFamTaxCreditElig(TestKey):

    """
    Benefit: Working for Families - Minimum Family Tax Credit (eligibility):

    If income.ofApplicantAndSpouse < 23816
        and 30 < applicant.worksWeeklyHours
            then benefit.isWorkingForFamiliesMinimumFamilyTaxCredit
                is PERMITTED

    Overriden by: Benefit: Working for Families - Minimum Family Tax Credit
        A. Forbidden if orphans benefit,
            Benefit: Working for Families - Minimum Family Tax Credit
        B. Forbidden if Unsupported Childs Benefit

    """

    body = {
        "applicant": {
            "worksWeeklyHours": 20
        },
        "benefit": {
            "isUnsupportedChildsBenefit": False,
            "isOrphansBenefit": False
        },
        "income": {
            "ofApplicantAndSpouse": 200
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)
        self.assertTrue(self.is_conclusive)
