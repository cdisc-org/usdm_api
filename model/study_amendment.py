from .api_base_model import ApiBaseModelWithId
from .study_amendment_reason import StudyAmendmentReason

class StudyAmendment(ApiBaseModelWithId):
  number: str
  summary: str
  substantialImpact: bool
  primaryReason: StudyAmendmentReason
  secondaryReason: StudyAmendmentReason
  enrollment: Enrollment
  previousId: str
