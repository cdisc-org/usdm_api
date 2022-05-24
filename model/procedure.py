from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class Procedure(ApiBaseModel):
  uuid: Union[str, None] = None
  procedure_name: str
  procedure_type: Union[Code, str, None]
  previous_procedure: Union[str, None] = None
  