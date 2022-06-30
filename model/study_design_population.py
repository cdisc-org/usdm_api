from typing import List, Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class StudyDesignPopulation(ApiBaseModel):
  uuid: Union[UUID, None] = None
  populationDesc: str
