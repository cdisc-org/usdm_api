from typing import Literal, List
from pydantic import Field
from .api_base_model import ApiBaseModelWithId
from .extension_attribute import ExtensionAttribute

class ExtensionClass(ApiBaseModelWithId):
  url: str = Field(min_length=1)
  attributes: List[ExtensionAttribute]
  instanceType: Literal['ExtensionClass']
