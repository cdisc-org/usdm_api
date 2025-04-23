from typing import Literal, Union
from .api_base_model import ApiBaseModelWithId
from .quantity import Quantity
from .range import Range

class QuantityRange(ApiBaseModelWithId):
  quantity: Union[Quantity, None] = None
  range: Union[Range, None] = None
  instanceType: Literal['QuantityRange']
