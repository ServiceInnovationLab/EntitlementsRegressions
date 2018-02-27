from . import Reasoner
import copy

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
            "Age": 21,
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
        self.assertTrue(self.is_permitted)


class TestEmployed(TestJobSeekerSupport):
    @property
    def body(self):
        new_body = copy.deepcopy(TestJobSeekerSupport.body)
        new_body.update({'applicant': {"employmentStatus": "full-time"}})
        return new_body

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)


class TestEmploymentNotStated(TestJobSeekerSupport):
    @property
    def body(self):
        new_body = copy.deepcopy(TestJobSeekerSupport.body)
        new_body['applicant'].pop("employmentStatus")
        return new_body

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)


class TestOverThreshold(TestJobSeekerSupport):
    @property
    def body(self):
        new_body = copy.deepcopy(TestJobSeekerSupport.body)
        new_body['threshold'].update({"income": {"JobSeekerSupport": False}})
        return new_body

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)


class TestNotPrepareForEmployment(TestJobSeekerSupport):
    @property
    def body(self):
        new_body = copy.deepcopy(TestJobSeekerSupport.body)
        new_body.update({"recipient": {"prepareForEmployment": False}})
        return new_body

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)


class TestTooYoung(TestJobSeekerSupport):
    @property
    def body(self):
        new_body = copy.deepcopy(TestJobSeekerSupport.body)
        new_body.update({'applicant': {"Age": 17}})
        return new_body

    def test_reasoning(self):

        self.assertTrue(self.is_forbidden)
