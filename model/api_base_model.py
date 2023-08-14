from pydantic import BaseModel, Field

class ApiBaseModel(BaseModel):
  pass

class ApiBaseModelWithId(ApiBaseModel):
  id: str = Field(min_length=1)

class ApiBaseModelWithIdAndName(ApiBaseModelWithId):
  name: str = Field(min_length=1)

class ApiBaseModelWithIdNameAndDesc(ApiBaseModelWithIdAndName):
  description: str = Field()

class ApiBaseModelWithIdAndDesc(ApiBaseModelWithId):
  description: str = Field()
