from typing import Union, List, Literal
from .api_base_model import ApiBaseModelWithIdOnly

class Extension(ApiBaseModelWithIdOnly):
  url: str

class ExtensionAttribute(Extension):
  valueString: Union[str,List[str]] = None
  valueBoolean: Union[bool,List[bool]] = None
  valueInteger: Union[int,List[int]] = None
  valueId: Union[str,List[str]] = None
  valueQuantity: Union['Quantity',List['Quantity']] = None
  valueRange: Union['Range',List['Range']] = None
  valueCode: Union['Code',List['Code']] = None
  valueAliasCode: Union['AliasCode',List['AliasCode']] = None
  valueExtensionClassInstance: Union['ExtensionClass',List['ExtensionClass']] = None
  instanceType: Literal['ExtensionAttribute']

class ExtensionClass(Extension):
  attributes: List[ExtensionAttribute]
  instanceType: Literal['ExtensionClass']

from .quantity import Quantity
from .range import Range
from .code import Code
from .alias_code import AliasCode