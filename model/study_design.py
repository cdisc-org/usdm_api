from typing import Union
from .code import Code
from .api_base_model import ApiBaseModel

class StudyDesign(ApiBaseModel):
  uuid: Union[str, None] = None
  trial_intent_type: Union[Code, str, None]
  trial_phase: Union[Code, str, None]
