from typing import Literal
from .api_base_model import ApiBaseModelWithId
from .organization import Organization

class StudyIdentifier(ApiBaseModelWithId):
  studyIdentifier: str
  studyIdentifierScope: Organization
  instanceType: Literal['StudyIdentifier']
