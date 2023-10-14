from pydantic import BaseModel, Field

class ApiBaseModel(BaseModel):
  pass

class ApiBaseModelWithId(ApiBaseModel):
  id: str = Field(min_length=1)

class ApiBaseModelWithIdAndDesc(ApiBaseModelWithId):
  description: str = ""

class ApiBaseModelWithIdAndName(ApiBaseModelWithId):
  name: str = Field(min_length=1)

class ApiBaseModelWithIdNameAndLabel(ApiBaseModelWithIdAndName):
  label: str = ""

class ApiBaseModelWithIdNameLabelAndDesc(ApiBaseModelWithIdNameAndLabel):
  description: str = ""

class ApiBaseModelWithIdNameAndDesc(ApiBaseModelWithIdAndName):
  description: str = ""
