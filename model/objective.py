from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .endpoint import Endpoint

class Objective(ApiBaseModel):
  id: str = constr(min_length=1)
  description: str = constr()
  objectiveLevel: Union[Code, None] = None
  objectiveEndpoints: List[Endpoint] = []