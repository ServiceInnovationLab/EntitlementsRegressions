from . import Reasoner


class TestHomeHelp(Reasoner):
    key = 'isHomeHelp'

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
                "HomeHelp": True
            },
            "cash": {
                "HomeHelp": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
