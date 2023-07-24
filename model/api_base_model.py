from pydantic import BaseModel, constr

class ApiBaseModel(BaseModel):
  pass

class ApiBaseModelWithId(ApiBaseModel):
  id: str = constr(min_length=1)

class ApiBaseModelWithIdAndName(ApiBaseModelWithId):
  name: str = constr(min_length=1)

class ApiBaseModelWithIdNameAndDesc(ApiBaseModelWithIdAndName):
  description: str = constr()

class ApiBaseModelWithIdAndDesc(ApiBaseModelWithId):
  description: str = constr()
