from typing import List
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class Indication(ApiBaseModelWithIdNameAndDesc):
  codes: List[Code] = []
