from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel
from .organisation import Organisation

class StudyIdentifier(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_identifier: str
  study_identifier_scope: Organisation

class StudyIdentifierResponse(ApiBaseModel):
  uuid: UUID
  study_identifier: str
  study_identifier_scope: UUID
