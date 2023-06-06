from typing import Union
from .api_base_model import ApiBaseModel

class TransitionRule(ApiBaseModel):
  transitionRuleId: str
  transitionRuleDescription: Union[str, None] = None
