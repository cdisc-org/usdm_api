from pydantic import constr
from typing import List
from .api_base_model import ApiBaseModel
from .code import Code

class Indication(ApiBaseModel):
  id: str = constr(min_length=1)
  description: str = constr()
  codes: List[Code] = []
