from . import Reasoner


class TestAccomodationSupplement(Reasoner):
    key = 'isAccommodationSupplement'

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
            "income": {
                "AccommodationSupplement": True
            },
            "cash": {
                "AccommodationSupplement": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
