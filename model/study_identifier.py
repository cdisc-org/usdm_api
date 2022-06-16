from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel
from .organisation import Organisation

class StudyIdentifier(ApiBaseModel):
  uuid: Union[UUID, None]
  studyIdentifier: str
  studyIdentifierScope: Union[UUID, Organisation]

  @classmethod
  def scope_reuse(cls):
    return True
