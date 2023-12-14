from .api_base_model import ApiBaseModel
from .organization import Organization
from typing import Literal

class StudyIdentifier(ApiBaseModel):
  studyIdentifier: str
  studyIdentifierScope: Organization
  instanceType: Literal['StudyIdentifier']