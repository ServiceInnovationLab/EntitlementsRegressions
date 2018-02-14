from . import Reasoner

"""


Benefit: Part 1D Child with Serious Disability (eligible):

If child.isDependent
    and child.hasSeriousDisability
    and child.requiresConstantCareAndAttention
    and child.hasMedicalCertification
    and applicant.isPrincipalCarer
    and applicant.isNZResident
then benefit.ChildDisabilityAllowance is PERMITTED

"""


class TestChildDisabilityAllowance(Reasoner):
    key = 'ChildDisabilityAllowance'

    body = {
        "applicant": {
            "isPrincipalCarer": True,
            "isNZResident": True
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "requiresConstantCareAndAttention": True,
            "hasMedicalCertification": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)


class TestChildDisabilityAllowanceWhenNotDisabled(Reasoner):
    key = 'ChildDisabilityAllowance'

    body = {
        "applicant": {
            "isPrincipalCarer": True,
            "isNZResident": True
        },
        "child": {
            "isDependent": True,
            # "hasSeriousDisability": True,
            # "requiresConstantCareAndAttention": True,
            # "hasMedicalCertification": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)
