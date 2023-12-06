from .api_base_model import ApiBaseModel
from .organization import Organization

class StudyIdentifier(ApiBaseModel):
  studyIdentifier: str
  studyIdentifierScope: Organization
