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
        response = self.runReason(body)
        print(response.text)
        assert_equal(response.json(), {})



if __name__ == '__main__':
    unittest.main()
