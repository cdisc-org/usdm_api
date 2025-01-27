from typing import Literal, List
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .extension_attribute import ExtensionAttribute

class ExtensionClass(ApiBaseModelWithIdNameLabelAndDesc):
  attributes: List[ExtensionAttribute]
  instanceType: Literal['ExtensionClass']
