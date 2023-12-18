from .api_base_model import ApiBaseModelWithId
from .organization import Organization
from typing import Literal

class StudyIdentifier(ApiBaseModelWithId):
  studyIdentifier: str
  studyIdentifierScope: Organization
  instanceType: Literal['StudyIdentifier'] = 'StudyIdentifier'