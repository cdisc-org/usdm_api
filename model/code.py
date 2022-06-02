from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel

class Code(ApiBaseModel):
  uuid: Union[UUID, None] = None
  code: str
  code_system: str
  code_system_version: str
  decode: str

class CodeResponse(ApiBaseModel):
  uuid: UUID
  code: str
  code_system: str
  code_system_version: str
  decode: str