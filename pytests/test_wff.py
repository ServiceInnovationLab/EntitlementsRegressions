from . import Reasoner
"""
Benefit: Working for Families - Family Tax Credit (eligibility):
If applicant.isParent
    and 20 ≤ applicant.worksWeeklyHours
    and not applicant.receivesIncomeTestedBenefit
    and not benefit.isStudentAllowance
    and applicant.isPrincipalCarer
    and not benefit.isOrphansBenefit is PERMITTED
    and not benefit.isUnsupportedChildsBenefit is PERMITTED
        then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
"""


class TestWorkingForFamilies(Reasoner):

    @property
    def test_basic(self):
        return {
            "applicant": {
                "isParent": True,
                "worksWeeklyHours": 19,
                "receivesIncomeTestedBenefit": False,
                "isPrincipalCarer": True
            },
            "benefit": {
                "isStudentAllowance": False
            },
            "threshold": {
                "income": {
                    "AccommodationSupplement": True
                },
                "cash": {
                    "AccommodationSupplement": True
                }
            }
        }

    def testNotEnoughInfo(self):
        response = self.runReason(self.not_enough_info).json()

        isWorkingForFamiliesFamilyTaxCredit = response.get(
            'benefit').get('isWorkingForFamiliesFamilyTaxCredit')

        self.assertEqual(len(isWorkingForFamiliesFamilyTaxCredit), 2)
        last_rule = isWorkingForFamiliesFamilyTaxCredit[-1]
        self.assertEqual(last_rule.get('reasoningResult'), 'CONCLUSIVE')
        self.assertEqual(last_rule.get('goal'), {
            "modality": "PERMITTED",
            "negated": False,
            "value": True,
            "id": "benefit.isWorkingForFamiliesFamilyTaxCredit",
            "type": "BOOL"
        })

    @property
    def not_enough_info(self):
        return {
            "applicant": {
                "Age": 30,
                "normallyLivesInNZ": True,
                "isNZResident": True,
                "hasAccommodationCosts": True,
                "hasSocialHousing": False,
                "receivesAccommodationSupport": False
            },
            "threshold": {
                "income": {
                    "AccommodationSupplement": True
                },
                "cash": {
                    "AccommodationSupplement": True
                }
            }
        }

    def testNotEnoughInfo(self):
        response = self.runReason(self.not_enough_info).json()

        isWorkingForFamiliesFamilyTaxCredit = response.get(
            'benefit').get('isWorkingForFamiliesFamilyTaxCredit')

        self.assertEqual(len(isWorkingForFamiliesFamilyTaxCredit), 2)
        last_rule = isWorkingForFamiliesFamilyTaxCredit[-1]
        self.assertEqual(last_rule.get('reasoningResult'), 'INCOMPLETE')
        # self.assertEqual(last_rule.get('goal'), {
        #     "modality": "PERMITTED",
        #     "negated": False,
        #     "value": True,
        #     "id": "benefit.isWorkingForFamiliesFamilyTaxCredit",
        #     "type": "BOOL"
        # })

if __name__ == '__main__':
    unittest.main()
