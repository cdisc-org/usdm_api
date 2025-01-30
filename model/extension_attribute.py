from typing import Literal
from pydantic import Field
from .api_base_model import ApiBaseModelWithId
from .quantity import Quantity
from .range import Range
from .code import Code
from .alias_code import AliasCode

class ExtensionAttribute(ApiBaseModelWithId):
  url: str = Field(min_length=1)
  valueString: str = None
  valueBoolean: bool = None
  valueInteger: int = None
  valueId: str = None
  valueQuantity: Quantity = None
  valueRange: Range = None
  valueCode: Code = None
  valueAliasCode: AliasCode = None
  instanceType: Literal['ExtensionAttribute']
