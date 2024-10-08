from .api_base_model import ApiBaseModelWithIdAndDesc
from .code import Code
from typing import Literal

class Masking(ApiBaseModelWithIdAndDesc):
  instanceType: Literal['Masking']
