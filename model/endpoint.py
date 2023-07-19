from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class Endpoint(ApiBaseModel):
  id: str = constr(min_length=1)
  description: str = constr()
  endpointPurposeDescription: str
  endpointLevel: Union[Code, None] = None
  