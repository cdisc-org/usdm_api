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

  @classmethod
  def search(cls, store, study_uuid):
    return store.get_by_klass_and_scope(cls.__name__, study_uuid)
