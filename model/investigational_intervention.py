from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class InvestigationalIntervention(ApiBaseModel):
  uuid: Union[str, None] = None
  intervention_desc: str
  intervention_status: str
  intervention_model: Union[List[Code], List[str], None]