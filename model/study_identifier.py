from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel
from .organisation import Organisation

class StudyIdentifier(ApiBaseModel):
  uuid: Union[UUID, None]
  study_identifier: str
  study_identifier_scope: Union[UUID, Organisation]

  @classmethod
  def scope_reuse(cls):
    return True
