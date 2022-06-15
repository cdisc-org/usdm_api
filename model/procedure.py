from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class Procedure(ApiBaseModel):
  uuid: Union[UUID, None] = None
  procedure_name: str
  procedure_type: Union[Code, UUID]
  previous_procedure: Union['Procedure', UUID, None] = None
  
  @classmethod
  def scope_reuse(cls):
    return True