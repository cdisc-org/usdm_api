from .api_base_model import ApiBaseModelWithId
from typing import Literal

class Code(ApiBaseModelWithId):
  code: str
  codeSystem: str
  codeSystemVersion: str
  decode: str
  instanceType: Literal['Code'] = 'Code'
