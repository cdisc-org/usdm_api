from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class PreviousProcedure(ApiBaseModel):
  procedureName: str
  procedureCode: Union[Code, UUID]

class Procedure(ApiBaseModel):
  procedureId: str
  procedureType: str
  procedureCode: Union[Code, UUID]
  
  @classmethod
  def scope_reuse(cls):
    return True