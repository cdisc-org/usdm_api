from typing import List
from .api_base_model import ApiBaseModelWithIdAndDesc
from .code import Code

class Indication(ApiBaseModelWithIdAndDesc):
  codes: List[Code] = []
