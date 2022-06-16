from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class PreviousProcedure(ApiBaseModel):
  procedure_name: str
  procedure_type: Union[Code, UUID]

class Procedure(ApiBaseModel):
  uuid: Union[UUID, None] = None
  procedure_name: str
  procedure_type: Union[Code, UUID]
  previous_procedure: Union[PreviousProcedure, UUID, None] = None
  
  @classmethod
  def scope_reuse(cls):
    return True