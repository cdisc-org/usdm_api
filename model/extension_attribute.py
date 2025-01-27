from typing import Literal
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .quantity import Quantity
from .range import Range
from .code import Code
from .alias_code import AliasCode

class ExtensionAttribute(ApiBaseModelWithIdNameLabelAndDesc):
  valueString: str = None
  valueBoolean: bool = None
  valueInteger: int = None
  valueId: str = None
  valueQuantity: Quantity = None
  valueRange: Range = None
  valueCode: Code = None
  valueAliasCode: AliasCode = None
  instanceType: Literal['ExtensionAttribute']
