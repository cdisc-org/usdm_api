from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel

class Code(ApiBaseModel):
  uuid: Union[UUID, None]
  code: str
  codeSystem: str
  codeSystemVersion: str
  decode: str
  
  @classmethod
  def global_reuse(cls):
    return True

