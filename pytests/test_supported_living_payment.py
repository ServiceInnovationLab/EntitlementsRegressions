from . import Reasoner


class TestSupportedLivingPaymentDefault(Reasoner):
    """
    Forbidden by default
    """
    key = 'isSupportedLivingPayment'
    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)


class TestSupportedLivingPaymentCarer(TestSupportedLivingPaymentDefault):
    """
    Benefit: Part 1E Supported Living Payment (eligible child carer applicant):
    If applicant.isPrincipalCarer
        and applicant.isNZResident
        and 16 ≤ applicant.Age
        and child.hasSeriousDisability
        and child.hasMedicalCertification
    then benefit.isSupportedLivingPayment is PERMITTED
    """

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


class TestSupportedLivingPaymentSelfAppl(TestSupportedLivingPaymentDefault):
    """
    Benefit: Part 1E Supported Living Payment (eligible self applicant):
    If applicant.isUnableToSupportThemselves
        and applicant.isNZResident
        and 16 ≤ applicant.Age
        and applicant.hasMedicalCertificate
        and applicant.hasSeriousDisability
    then benefit.isSupportedLivingPayment is PERMITTED
    """

    body = {
        "applicant": {
            "isUnableToSupportThemselves": True,
            "isNZResident": True,
            "Age": 45,
            "hasMedicalCertificate": True,
            "hasSeriousDisability": True
        }
    }


class TestSupportedLivingPaymentAmbigious(TestSupportedLivingPaymentDefault):
    body = {
        "applicant": {
            "isUnableToSupportThemselves": True,
            "isNZResident": True,
            # "Age": 15,
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "hasMedicalCertification": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)


class TestSupportedLivingTooYoung(TestSupportedLivingPaymentDefault):
    body = {
        "applicant": {
            "isUnableToSupportThemselves": True,
            "isNZResident": True,
            "Age": 15
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "hasMedicalCertification": True
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_forbidden)
