from . import Reasoner

"""
Benefit: Young Parent Payment (eligibility):
    If 16 ≤ applicant.Age
        and applicant.Age ≤ 19
        and child.isDependent
        and applicant.isNZResident
        and applicant.normallyLivesInNZ
        and applicant.isParent
        and not benefit.isOrphansBenefit
        and not benefit.isUnsupportedChildsBenefit
        and 1 ≤ applicant.numberOfChildren
        and threshold.income.YoungParentPayment
    then benefit.isYoungParentPayment is PERMITTED
"""


class TestYoungParentPayment(Reasoner):
    key = 'isYoungParentPayment'

    body = {
        "applicant": {
            "Age": 16,
            "isNZResident": True,
            "normallyLivesInNZ": True,
            "isParent": True,
            "numberOfChildren": 1
        },
        "child": {
            "isDependent": True
        },
        "benefit": {
            "isOrphansBenefit": False,
            "isUnsupportedChildsBenefit": False
        },
        "threshold": {
            "income": {
                "YoungParentPayment": True
            }
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_permitted)
