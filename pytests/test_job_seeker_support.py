from . import Reasoner

"""
Benefit: JobSeeker Support (eligibility):
    If applicant.employmentStatus ≠ "full-time"
        and 18 ≤ applicant.Age
        and applicant.isNZResident
        and applicant.hasLivedInNZfor2Years
        and applicant.normallyLivesInNZ
        and recipient.prepareForEmployment
        and threshold.income.JobSeekerSupport
    then benefit.isJobSeekerSupport is PERMITTED
"""


class TestJobSeekerSupport(Reasoner):
    key = 'isJobSeekerSupport'

    body = {
        "applicant": {
            "employmentStatus": "part-time",
            "Age": 18,
            "hasLivedInNZfor2Years": True,
            "isNZResident": True,
            "normallyLivesInNZ": True
        },
        "income": {
            "ofApplicantAndSpouse": 550
        },
        "recipient": {
            "prepareForEmployment": True
        },
        "threshold": {
            "income": {
                "JobSeekerSupport": True
            }
        }
    }

    def test_reasoning(self):
        self.assertTrue(self.is_conclusive)
        self.assertTrue(self.is_permitted)
