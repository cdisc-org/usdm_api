from typing import Union
from .api_base_model import ApiBaseModel
from .rule import Rule
from uuid import UUID

class StudyElement(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyElementName: str
  studyElementDesc: str
  startRule: Union[Rule, UUID, None] = None
  endRule: Union[Rule, UUID, None] = None
