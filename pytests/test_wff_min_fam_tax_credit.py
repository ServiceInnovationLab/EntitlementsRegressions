from . import Reasoner


class TestKey(Reasoner):
    key = 'isWorkingForFamiliesMinimumFamilyTaxCredit'


"""
Benefit: Working for Families - Minimum Family Tax Credit (default state):
Default benefit.isWorkingForFamiliesMinimumFamilyTaxCredit is FORBIDDEN
Overriden by: Benefit: Working for Families - Minimum Family Tax Credit
(eligibility)
"""


class TestWFFMinimumFamilyTC(TestKey):

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)  # FIXME:should be forbidden


"""
Benefit: Working for Families - Minimum Family Tax Credit (eligibility):
If income.ofApplicantAndSpouse < 23816
and applicant.worksWeeklyHours < 30
then benefit.isWorkingForFamiliesMinimumFamilyTaxCredit is PERMITTED
    Overriden by: Benefit: Working for Families - Minimum Family Tax Credit
    A. Forbidden if orphans benefit, Benefit: Working for Families
        - Minimum Family Tax Credit
    B. Forbidden if Unsupported Childs Benefit
"""


class TestWFFMinimumFamilyTC(TestKey):

    body = {
        "income": {
            "ofApplicantAndSpouse": 2000
        },
        "applicant": {
            "worksWeeklyHours": 20
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)  # Working
