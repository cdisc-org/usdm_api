from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .endpoint import Endpoint

class Objective(ApiBaseModel):
  uuid: Union[str, None] = None
  objective_desc: str
  objective_level: Union[List[Code], List[str], None]
  objective_endpoints: Union[List[Endpoint], List[str], None]