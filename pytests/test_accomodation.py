from . import Reasoner


class TestAccomodationSupplement(Reasoner):

    @property
    def basic_body(self):
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

    def testBasic(self):
        response = self.runReason(self.basic_body).json()

        isAccommodationSupplement = response.get(
            'benefit').get('isAccommodationSupplement')

        self.assertEqual(len(isAccommodationSupplement), 3)
        last_rule = isAccommodationSupplement[-1]
        self.assertEqual(last_rule.get('reasoningResult'), 'CONCLUSIVE')
        self.assertEqual(last_rule.get('goal'), {
            "modality": "PERMITTED",
            "negated": False,
            "value": True,
            "id": "benefit.isAccommodationSupplement",
            "type": "BOOL"
        })

if __name__ == '__main__':
    unittest.main()
