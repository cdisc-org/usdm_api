from typing import List, Union
from .api_base_model import ApiBaseModel
from .population import Population

class Estimand(ApiBaseModel):
  uuid: Union[str, None] = None
  summary_measure: str
  population: Union[Population, str, None]
