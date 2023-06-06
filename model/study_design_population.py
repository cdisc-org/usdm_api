from typing import List, Union
from pydantic import NonNegativeInt
from .api_base_model import ApiBaseModel
from .code import Code

class StudyDesignPopulation(ApiBaseModel):
  studyDesignPopulationId: str
  populationDescription: Union[str, None] = None
  plannedNumberOfParticipants: NonNegativeInt
  plannedMaximumAgeOfParticipants: str  
  plannedMinimumAgeOfParticipants: str
  plannedSexOfParticipants: List[Code] = []
