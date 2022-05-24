from typing import Union
from .api_base_model import ApiBaseModel
from .rule import Rule
from uuid import uuid4

class StudyElement(ApiBaseModel):
  uuid: Union[str, None] = None
  study_element_desc: str
  study_element_name: str
  start_rule: Union[Rule, str, None] = None
  end_rule: Union[Rule, str, None] = None
