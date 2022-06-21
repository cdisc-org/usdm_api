from typing import Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class TransitionRule(ApiBaseModel):
  uuid: Union[UUID, None] = None
  transitionRuleDesc: str