from pydantic import BaseModel, Field, constr

class ApiBaseModel(BaseModel):
  pass

class ApiBaseModelWithId(ApiBaseModel):
  id: str = Field(min_length=1)

class ApiBaseModelWithIdAndDesc(ApiBaseModelWithId):
  description: str = constr()

class ApiBaseModelWithIdAndName(ApiBaseModelWithId):
  name: str = Field(min_length=1)

class ApiBaseModelWithIdNameAndLabel(ApiBaseModelWithIdAndName):
  label: str = constr()

class ApiBaseModelWithIdNameLabelAndDesc(ApiBaseModelWithIdNameAndLabel):
  description: str = constr()

class ApiBaseModelWithIdNameAndDesc(ApiBaseModelWithIdAndName):
  description: str = constr()
