from typing import Union
from pydantic import BaseModel, Field

class ApiBaseModel(BaseModel):
  pass

class ApiBaseModelWithId(ApiBaseModel):
  id: str = Field(min_length=1)

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
