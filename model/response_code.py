from .api_base_model import ApiBaseModelWithId
from .code import Code
from typing import Literal

class ResponseCode(ApiBaseModelWithId):
  isEnabled: bool
  code: Code
  instanceType: Literal['ResponseCode']
