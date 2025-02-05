from typing import Union, List, Literal
from .api_base_model import ApiBaseModelWithIdOnly

class Extension(ApiBaseModelWithIdOnly):
  url: str

class ExtensionAttribute(Extension):
  # values or extensions, never both.
  valueString: str = None
  valueBoolean: bool = None
  valueInteger: int = None
  valueId: str = None
  valueQuantity: 'Quantity' = None
  valueRange: 'Range' = None
  valueCode: 'Code' = None
  valueAliasCode: 'AliasCode' = None
  extensionAttributes: List['ExtensionAttribute'] = [] # Could be named attributes, named to align woth ApiBaseModelWithId definition
  instanceType: Literal['ExtensionAttribute']

class ExtensionClass(Extension):
  extensionAttributes: List['ExtensionAttribute'] = [] # Could be named attributes, named to align woth ApiBaseModelWithId definition and above
  instanceType: Literal['ExtensionClass']

from .quantity import Quantity
from .range import Range
from .code import Code
from .alias_code import AliasCode