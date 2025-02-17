from __future__ import annotations
from typing import Union, List
from pydantic import BaseModel, Field

class ApiBaseModel(BaseModel):
  pass

class ApiBaseModelWithIdOnly(ApiBaseModel):
  id: str = Field(min_length=1)

class ApiBaseModelWithId(ApiBaseModelWithIdOnly):
  extensionAttributes: List['ExtensionAttribute'] = []

from .extension import ExtensionAttribute

class ApiBaseModelWithIdAndDesc(ApiBaseModelWithId):
  description: Union[str, None] = None

class ApiBaseModelWithIdAndName(ApiBaseModelWithId):
  name: str = Field(min_length=1)

class ApiBaseModelWithIdNameAndLabel(ApiBaseModelWithIdAndName):
  label: Union[str, None] = None

class ApiBaseModelWithIdNameLabelAndDesc(ApiBaseModelWithIdNameAndLabel):
  description: Union[str, None] = None

class ApiBaseModelWithIdNameAndDesc(ApiBaseModelWithIdAndName):
  description: Union[str, None] = None
