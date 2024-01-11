from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from typing import Literal

class IntercurrentEvent(ApiBaseModelWithIdNameLabelAndDesc):
  strategy: str
  instanceType: Literal['IntercurrentEvent']
