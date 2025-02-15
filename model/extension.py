from typing import List, Literal
from .api_base_model import ApiBaseModelWithIdOnly

class Extension(ApiBaseModelWithIdOnly):
  url: str

class ExtensionAttribute(Extension):
  # values or extension attributes, never both.
  valueString: str = None
  valueBoolean: bool = None
  valueInteger: int = None
  valueId: str = None
  valueQuantity: 'Quantity' = None
  valueRange: 'Range' = None
  valueCode: 'Code' = None
  valueAliasCode: 'AliasCode' = None
  valueExtensionClass: 'ExtensionClass' = None
  extensionAttributes: List['ExtensionAttribute'] = []
  instanceType: Literal['ExtensionAttribute']

class ExtensionClass(Extension):
  extensionAttributes: List['ExtensionAttribute'] = []
  instanceType: Literal['ExtensionClass']

from .quantity import Quantity
from .range import Range
from .code import Code
from .alias_code import AliasCode