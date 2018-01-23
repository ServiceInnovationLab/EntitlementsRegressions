from . import Reasoner


class TestAccomodationSupplement(Reasoner):

    def testTahi(self):
        body = {
            "applicant": {
                "Age": 30,
                "normallyLivesInNZ": True,
                "isNZResident": True,
                "hasAccommodationCosts": True,
                "hasSocialHousing": False,
                "receivesAccommodationSupport": False
            },
            "threshold": {
                "isAccommodationSupplement": True
            },
            "benefit": {
                "isStudentAllowance": False
            }
        }
        response = self.runReason(body).json()

        isAccommodationSupplement = response.get(
            'benefit').get('isAccommodationSupplement')
        print(isAccommodationSupplement)
        self.assertTrue(len(isAccommodationSupplement) > 0)


if __name__ == '__main__':
    unittest.main()
