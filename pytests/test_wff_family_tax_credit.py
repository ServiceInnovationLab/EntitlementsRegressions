from . import Reasoner
from .test_unsupported_childs_benefit import TestUnsupportedChildsBenefit


class TestWFFTaxCreditKey(Reasoner):
    key = 'isWorkingForFamiliesFamilyTaxCredit'


class TestWFFTaxCreditDefault(TestWFFTaxCreditKey):

    """
    For families with dependent children

    Benefit: Working for Families - Family Tax Credit (default state):
    Default benefit.isWorkingForFamiliesFamilyTaxCredit is FORBIDDEN
    Overriden by: Benefit: Working for Families
     - Family Tax Credit (eligibility)
    """

    body = {}

    def test_reasoning(self):
        self.assertTrue(self.is_forbidden)


class TestWFF_FamilyTaxCredit(TestWFFTaxCreditKey):
    """
    If applicant.isParent
        and applicant.isPrincipalCarer
        and threshold.income.WorkingForFamiliesFamilyTaxCredit
    then benefit.isWorkingForFamiliesFamilyTaxCredit is PERMITTED
    """
    body = {
        "applicant": {
            "isNZResident": True,
            "isParent": True,
            "isPrincipalCarer": True,
        },
        "child": {
            "isDependent": True
        },
        "threshold": {
            "income": {
                "WorkingForFamiliesFamilyTaxCredit": True
            }
        }
    }

    def test_permitted_workingforfamiliesfamilytaxcredit(self):
        self.assertTrue(self.isPermitted(self.key))

    def test_forbidden_student_allowance(self):
        self.assertTrue(self.isForbidden('isStudentAllowance'))

    def test_forbidden_orphans(self):
        self.assertTrue(self.isForbidden('isOrphansBenefit'))

    def test_forbidden_unsupported_child(self):
        self.assertTrue(self.isForbidden('isUnsupportedChildsBenefit'))


class TestWFF_FamilyTaxCreditUnsupportedChild(TestWFFTaxCreditKey):
    """
    Overridden to forbidden if eligible for:
        benefit.isOrphansBenefit
        benefit.isUnsupportedChildsBenefit
        benefit.isStudentAllowance
    """

    body = {
        **TestWFF_FamilyTaxCredit.body,
        **TestUnsupportedChildsBenefit.body
    }

    def test_forbidden_workingforfamiliesfamilytaxcredit(self):
        self.assertTrue(self.isForbidden(self.key))

    def test_permitted_unsupported_child(self):
        self.assertTrue(self.isPermitted('isUnsupportedChildsBenefit'))
