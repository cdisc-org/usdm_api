from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class InvestigationalIntervention(ApiBaseModel):
  investigationalInterventionId: str
  interventionDesc: str
  codes: Union[List[Code], List[UUID], None]  
