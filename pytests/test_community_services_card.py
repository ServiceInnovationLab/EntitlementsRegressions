from . import Reasoner

"""
Benefit: Community Services Card (eligibility):
    If 16 ≤ applicant.Age
        and applicant.isNZResident
        and applicant.normallyLivesInNZ
        and threshold.isCommunityServicesCard
            then benefit.isCommunityServicesCard is PERMITTED
"""

class TestCommunityServicesCard(Reasoner):
    key = 'isCommunityServicesCard'

    body = {
        "applicant": {
            "Age": 17,
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "hasSeriousDisability": True
        },
        "threshold": {
            "isCommunityServicesCard": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
