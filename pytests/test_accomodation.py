from . import Reasoner


class TestAccomodationSupplement(Reasoner):

    def testBasic(self):
        body = {
            "applicant": {
                "Age": 30,
                "normallyLivesInNZ": true,
                "isNZResident": true,
                "hasAccommodationCosts": true,
                "hasSocialHousing": false,
                "receivesAccommodationSupport": false
            },
            "threshold": {
                "income": {
                    "AccommodationSupplement": true
                },
                "cash": {
                    "AccommodationSupplement": true
                }
            }
        }
        response = self.runReason(body).json()

        isAccommodationSupplement = response.get(
            'benefit').get('isAccommodationSupplement')
        # print(isAccommodationSupplement)
        self.assertTrue(len(isAccommodationSupplement) > 0)
        conclusive = self.findConclusive(isAccommodationSupplement)
        # print(conclusive.keys())
        # self.assertEqual(conclusive.get('goal').get('id'), 'benefit.isAccommodationSupplement')
        # self.assertEqual(conclusive.get('goal').get('modality'), 'PERMITTED')
        expected = {
            "dependencies": {
                "factsUsed": [
                    "applicant.normallyLivesInNZ",
                    "applicant.isNZResident",
                    "applicant.hasAccommodationCosts",
                    "applicant.hasSocialHousing",
                    "applicant.receivesAccommodationSupport"
                ],
                "rulesUsed": [
                    "f-7683c46f-8502-44a7-b980-d235a13747eb"
                ]
            },
            "goal": {
                "modality": "FORBIDDEN",
                "negated": False,
                "value": True,
                "id": "benefit.isAccommodationSupplement",
                "type": "BOOL"
            },
            "reasoningResult": "CONCLUSIVE"
        }
        print(isAccommodationSupplement.keys())
        self.assertTrue(expected in isAccommodationSupplement)


if __name__ == '__main__':
    unittest.main()
