from typing import Union
from .api_base_model import ApiBaseModel

class Rule(ApiBaseModel):
  uuid: Union[str, None] = None
  rule_desc: str