from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class IntercurrentEvent(ApiBaseModel):
  uuid: Union[str, None] = None
  intercurrent_name: str
  intercurrent_desc: str
  coding: Union[Code, str, None]
