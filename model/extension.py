from typing import Union, List, Literal
from .api_base_model import ApiBaseModelWithIdOnly

class Extension(ApiBaseModelWithIdOnly):
  url: str

class ExtensionAttribute(Extension):
  # values or extension attributes, never both.
  valueString: Union[str, None] = None
  valueBoolean: Union[bool, None] = None
  valueInteger: Union[int, None] = None
  valueId: Union[str, None] = None
  valueQuantity: Union['Quantity', None] = None
  valueRange: Union['Range', None] = None
  valueCode: Union['Code', None] = None
  valueAliasCode: Union['AliasCode', None] = None
  valueExtensionClass: Union['ExtensionClass', None] = None
  extensionAttributes: List['ExtensionAttribute'] = []
  instanceType: Literal['ExtensionAttribute']

class ExtensionClass(Extension):
  extensionAttributes: List['ExtensionAttribute'] = []
  instanceType: Literal['ExtensionClass']

from .quantity import Quantity
from .range import Range
from .code import Code
from .alias_code import AliasCode