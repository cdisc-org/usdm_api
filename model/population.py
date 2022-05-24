from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .endpoint import Endpoint

class Population(ApiBaseModel):
  uuid: Union[str, None] = None
  population_desc: str
