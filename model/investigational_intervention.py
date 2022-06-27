from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class InvestigationalIntervention(ApiBaseModel):
  uuid: Union[UUID, None] = None
  interventions: Union[List[Code], List[UUID], None]  
  interventionDesc: str
  interventionModel: Union[Code, UUID]