from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from .rule import Rule

class Encounter(ApiBaseModel):
  uuid: Union[str, None] = None
  encounter_desc: str
  name: str
  encounter_type: Union[Code, str, None]
  env_setting: Union[Code, str, None]
  contact_mode: Union[Code, str, None]
  start_rule: Union[Rule, str, None] = None
  end_rule: Union[Rule, str, None] = None