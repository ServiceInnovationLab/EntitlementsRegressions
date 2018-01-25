from . import Reasoner


class TestHomeHelpDisability(Reasoner):

    @property
    def basic_body(self):
        return {
            "applicant": {
                "Age": 30,
                "normallyLivesInNZ": True,
                "isNZResident": True,
                "hasSeriousDisability": True,
                "holdsCommunityServicesCard": True,
                "needsDomesticSupport": True
            },
            "threshold": {
                "cash": {
                    "HomeHelp": True
                }
            }
        }

    def testBasic(self):
        response = self.runReason(self.basic_body).json()

        isHomeHelp = response.get(
            'benefit').get('isHomeHelp')

        self.assertEqual(len(isHomeHelp), 2)
        last_rule = isHomeHelp[-1]
        self.assertEqual(last_rule.get('reasoningResult'), 'CONCLUSIVE')
        self.assertEqual(last_rule.get('goal'), {
            "modality": "PERMITTED",
            "negated": False,
            "value": True,
            "id": "benefit.isHomeHelp",
            "type": "BOOL"
        })

if __name__ == '__main__':
    unittest.main()
