from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel
from .code import Code

class StudyIdentifier(ApiBaseModel):
  uuid: Union[str, None] = None
  study_identifier: str
  study_identifier_type: Code
  organization_name: str

class StudyIdentifierResponse(ApiBaseModel):
  uuid: UUID
  study_identifier: str
  study_identifier_type: UUID
  organization_name: str