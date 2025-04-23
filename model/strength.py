from typing import Literal, Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .quantity import Quantity
from .quantity_range import QuantityRange

class Strength(ApiBaseModelWithIdNameLabelAndDesc):
  numerator: QuantityRange
  denominator: Union[Quantity, None] = None
  instanceType: Literal['Strength']
