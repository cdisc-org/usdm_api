from typing import Union
from .api_base_model import ApiBaseModel

class Code(ApiBaseModel):
  uuid: Union[str, None] = None
  code: str
  code_system: str
  code_system_version: str
  decode: str