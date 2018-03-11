from . import Reasoner


"""
Benefit: Childcare subsidy:Default benefit.isChildCareSubsidy is FORBIDDEN
Overriden by:
Benefit: Childcare subsidy (eligibility for disabled under 6s),
Benefit: Childcare subsidy (eligibility for under 5s)
"""


class TestChildSubsidyDefault(Reasoner):
    key = 'isChildCareSubsidy'

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


"""
Benefit: Childcare subsidy (eligibility for disabled under 6s):
If child.Age < 6
    and benefit.ChildDisabilityAllowance
    and applicant.isPrincipalCarer
    and threshold.income.ChildCareSubsidy
    and applicant.isNZResident
    and 3 ≤ child.WeeklyECEHours
    and 1 ≤ applicant.numberOfChildren
then benefit.isChildCareSubsidy is PERMITTED
"""


class ChildCareSubsidyDisabledUnder6s(Reasoner):

    key = 'isChildCareSubsidy'

    body = {
        "child": {
            "Age": 5,
            "hasMedicalCertification": True,
            "hasSeriousDisability": True,
            "isDependent": True,
            "requiresConstantCareAndAttention": True,
            "WeeklyECEHours": 4,
        },
        "applicant": {
            "numberOfChildren": 3,
            "isNZResident": True,
            "isPrincipalCarer": True,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "threshold": {
            "income": {
                "ChildCareSubsidy": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_permitted)


"""
Benefit: Childcare subsidy (eligibility for under 5s):
If child.Age < 5
    and applicant.isPrincipalCarer
    and threshold.income.ChildCareSubsidy
    and applicant.isNZResident
    and 3 ≤ child.WeeklyECEHours
    and 1 ≤ applicant.numberOfChildren
then benefit.isChildCareSubsidy is PERMITTED
"""


class ChildCareSubsidyUnder5s(Reasoner):

    key = 'isChildCareSubsidy'

    body = {
        "child": {
            "Age": 4,
            "WeeklyECEHours": 4
        },
        "applicant": {
            "numberOfChildren": 3,
            "isNZResident": True,
            "isPrincipalCarer": True
        },
        "threshold": {
            "income": {
                "ChildCareSubsidy": True
            }
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_permitted)
