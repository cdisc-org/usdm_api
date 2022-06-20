from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class PreviousProcedure(ApiBaseModel):
  procedureName: str
  procedureCode: Union[Code, UUID]

class Procedure(ApiBaseModel):
  uuid: Union[UUID, None] = None
  procedureType: str
  procedureCode: Union[Code, UUID]
  previousProcedure: Union[PreviousProcedure, UUID, None] = None
  
  @classmethod
  def scope_reuse(cls):
    return True