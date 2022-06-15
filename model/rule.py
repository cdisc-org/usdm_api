from typing import Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class Rule(ApiBaseModel):
  uuid: Union[UUID, None] = None
  rule_desc: str