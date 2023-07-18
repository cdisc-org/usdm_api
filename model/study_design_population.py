from typing import List
from pydantic import constr, NonNegativeInt
from .api_base_model import ApiBaseModel
from .code import Code

class StudyDesignPopulation(ApiBaseModel):
  id: str = constr(min_length=1)
  description: str = constr()
  plannedNumberOfParticipants: NonNegativeInt
  plannedMaximumAgeOfParticipants: str  
  plannedMinimumAgeOfParticipants: str
  plannedSexOfParticipants: List[Code] = []
