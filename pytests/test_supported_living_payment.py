from . import Reasoner


class TestSupportedLivingPaymentDefault(Reasoner):
    """
    Forbidden by default
    """
    key = 'isSupportedLivingPayment'
    body = {}

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)


class TestSupportedLivingPaymentCarer(Reasoner):
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

        self.assertTrue(self.is_permitted)


class TestSupportedLivingPaymentSelfAppl(Reasoner):
    """
    Benefit: Part 1E Supported Living Payment (eligible self applicant):
    If applicant.isNZResident
        and 16 ≤ applicant.Age
        and applicant.hasMedicalCertificate
        and applicant.hasSeriousDisability
        and threshold.income.SupportedLivingPayment
    then benefit.isSupportedLivingPayment is PERMITTED
    """

    key = 'isSupportedLivingPayment'
    body = {
        "applicant": {
            "isNZResident": True,
            "Age": 45,
            "hasMedicalCertificate": True,
            "hasSeriousDisability": True
        },
        "threshold": {
            "income": {
                "SupportedLivingPayment": True
            }
        }
    }


class TestSupportedLivingPaymentAmbigious(Reasoner):
    key = 'isSupportedLivingPayment'
    body = {
        "applicant": {
            "isNZResident": True,
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "hasMedicalCertification": True
        },
        "threshold": {
            "income": {
                "SupportedLivingPayment": True
            }
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)


class TestSupportedLivingTooYoung(Reasoner):
    key = 'isSupportedLivingPayment'
    body = {
        "applicant": {
            "isNZResident": True,
            "Age": 15
        },
        "child": {
            "isDependent": True,
            "hasSeriousDisability": True,
            "hasMedicalCertification": True
        },
        "threshold": {
            "income": {
                "SupportedLivingPayment": True
            }
        }
    }

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)
