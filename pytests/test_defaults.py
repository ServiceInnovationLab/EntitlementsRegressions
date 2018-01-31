from . import Reasoner


class TestDefaults(Reasoner):

    smartStartBenefits = [
        'isAccommodationSupplement',
        'ChildDisabilityAllowance',
        'isCommunityServicesCard',
        'isHomeHelp',
        'isJobSeekerSupport',
        'isOrphansBenefit',
        'isSoleParentSupport',
        'isStudentAllowance',
        'isUnsupportedChildsBenefit',
        'isWorkingForFamiliesFamilyTaxCredit',
        'isYoungParentPayment'
    ]

    for benefit in smartStartBenefits:

        key = benefit

        body = {}

        def test_reasoning(self):
            self.assertTrue(self.is_conclusive)
            self.assertTrue(self.is_forbidden)
