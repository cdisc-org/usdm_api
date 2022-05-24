from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class Estimand(ApiBaseModel):
  uuid: Union[str, None] = None
  summary_measure: str
  population: Union[Code, str, None]
