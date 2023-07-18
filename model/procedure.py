from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class Procedure(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  procedureDescription: Union[str, None] = None
  procedureCode: Code
  procedureIsConditional: bool
  procedureIsConditionalReason: Union[str, None] = None
