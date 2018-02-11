# from . import Reasoner


# class TestKey(Reasoner):
#     key = 'ChildDisabilityAllowance'


# """
# Benefit: Part 1D Child with Serious Disability (eligible):
# If child.isDependent
#     and child.hasSeriousDisability
#     and child.requiresConstantCare
#     and child.hasMedicalCertification
#     and applicant.isPrincipalCarer
#     and applicant.isNZResident
#         then benefit.ChildDisabilityAllowance is PERMITTED

# """


# class TestChildDisabilityAllowance(TestKey):

#     body = {
#         "applicant": {
#             "isPrincipalCarer": True,
#             "isNZResident": True
#         },
#         "child": {
#             "isFinanciallyIndependent": True,
#             "hasSeriousDisability": True,
#             "requiresConstantCare": True,
#             "hasMedicalCertification": True
#         }
#     }

#     def test_reasoning(self):
#         self.assertTrue(self.is_conclusive)
#         self.assertTrue(self.is_permitted)


# class TestChildDisabilityAllowanceWhenNotDisabled(TestKey):

#     body = {
#         "applicant": {
#             "isPrincipalCarer": True,
#             "isNZResident": True
#         },
#         "child": {
#             "isFinanciallyIndependent": True
#         }
#     }

#     def test_reasoning(self):
#         self.assertTrue(self.is_conclusive)
#         self.assertTrue(self.is_forbidden)
