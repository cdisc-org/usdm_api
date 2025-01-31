from typing import Literal, Union
from .api_base_model import ApiBaseModelWithIdAndDesc
from .quantity import Quantity

class AdministrationDuration(ApiBaseModelWithIdAndDesc):
  quantity:	Union[Quantity, None] = None
  durationWillVary: bool
  reasonDurationWillVary:	Union[str, None] = None
  instanceType: Literal['AdministrationDuration']
