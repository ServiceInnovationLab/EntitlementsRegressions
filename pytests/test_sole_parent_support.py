from . import Reasoner
from pprint import pprint
"""
Benefit: Part 1B Sole Parent Support (eligibility in legislation):
If applicant.isParent
    and applicant.isInadequatelySupportedByPartner
    and applicant.isMaintainingChild
    and applicant.isNZResident
    and 20 ≤ applicant.Age
    and child.Age < 14
    and child.isDependent
    and (income.ofApplicantAndSpouse + income.fromMaintenancePayments) < 628
        then benefit.isSoleParentSupport is PERMITTED

    If not benefit.ChildDisabilityAllowance
        and not benefit.isSoleParentSupport
        and not benefit.isOrphansBenefit
        and not benefit.isSupportedLivingPayment
        and not benefit.isUnsupportedChildsBenefit
        and applicant.isUnableToSupportThemselves
        and not benefit.ChildDisabilityAllowance
        and not benefit.isAccommodationSupplement
        and applicant.isNZResident
        and applicant.normallyLivesInNZ
            then benefit.isEmergencyBenefit is PERMITTED
"""

class TestSoleParentSupport(Reasoner):
    key = 'isSoleParentSupport'

    body = {
        "applicant": {
            "normallyLivesInNZ": True,
            "isNZResident": True,
            "isParent": True,
            "isMaintainingChild": True,
            "isUnableToSupportThemselves": True
        },
        "child": {
            "isDependent": True
        },
        "benefit": {
            "ChildDisabilityAllowance": False,
            "isSoleParentSupport": False,
            "isOrphansBenefit": False,
            "isSupportedLivingPayment": False,
            "isUnsupportedChildsBenefit": False,
            "ChildDisabilityAllowance": False,
            "isAccommodationSupplement": False
        }

    }

    def test_reasoning(self):
        pprint(self.subject)
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)

