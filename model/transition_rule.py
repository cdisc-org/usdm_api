from pydantic import constr
from .api_base_model import ApiBaseModel

class TransitionRule(ApiBaseModel):
  id: str = constr(min_length=1)
  description: str = constr()
