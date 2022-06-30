from typing import List, Union
from .api_base_model import ApiBaseModel

class AnalysisPopulation(ApiBaseModel):
  uuid: Union[str, None] = None
  populationDesc: str
