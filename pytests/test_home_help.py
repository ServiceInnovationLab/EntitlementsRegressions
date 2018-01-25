from . import Reasoner

"""
Benefit: Home Help (eligibility in policy for applicant with disability):
    If applicant.isNZResident
        and applicant.normallyLivesInNZ
        and applicant.needsDomesticSupport
        and applicant.hasSeriousDisability
        and threshold.cash.HomeHelp
        and applicant.holdsCommunityServicesCard
            then benefit.isHomeHelp is PERMITTED
"""


class TestHomeHelp(Reasoner):
    key = 'isHomeHelp'

    body = {
        "applicant": {
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "needsDomesticSupport": True,
            "hasSeriousDisability": True,
            "holdsCommunityServicesCard": True
        },
        "threshold": {
            "cash": {
                "HomeHelp": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
