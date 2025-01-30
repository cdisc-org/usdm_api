from typing import Literal, List
from .api_base_model import ApiBaseModelWithId
from .extension_attribute import ExtensionAttribute

class ExtensionClass(ApiBaseModelWithId):
  attributes: List[ExtensionAttribute]
  instanceType: Literal['ExtensionClass']
