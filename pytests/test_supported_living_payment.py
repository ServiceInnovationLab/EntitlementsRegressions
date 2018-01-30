from . import Reasoner


class TestSupportedLivingPayment(Reasoner):
    """
    Benefit: Part 1E Supported Living Payment (eligible child carer applicant):
    If applicant.isPrincipalCarer
        and applicant.isNZResident
        and 16 ≤ applicant.Age
        and child.hasSeriousDisability
        and child.hasMedicalCertification
    then benefit.isSupportedLivingPayment is PERMITTED
    """

    key = 'isSupportedLivingPayment'

    body = {
        "applicant": {
            "isPrincipalCarer": True,
            "isNZResident": True,
            "Age": 45
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "hasMedicalCertification": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)


class TestSupportedLivingPayment(Reasoner):
    """
    Benefit: Part 1E Supported Living Payment (eligible self applicant):
    If applicant.isUnableToSupportThemselves
        and applicant.isNZResident
        and 16 ≤ applicant.Age
        and applicant.hasMedicalCertificate
        and applicant.hasSeriousDisability
    then benefit.isSupportedLivingPayment is PERMITTED
    """

    key = 'isSupportedLivingPayment'

    body = {
        "applicant": {
            "isUnableToSupportThemselves": True,
            "isNZResident": True,
            "Age": 45,
            "hasMedicalCertificate": True,
            "hasSeriousDisability": True
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "hasMedicalCertification": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
