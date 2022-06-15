from typing import Union
from .api_base_model import ApiBaseModel
from .rule import Rule
from uuid import UUID

class StudyElement(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_element_name: str
  study_element_desc: str
  start_rule: Union[Rule, UUID, None] = None
  end_rule: Union[Rule, UUID, None] = None
