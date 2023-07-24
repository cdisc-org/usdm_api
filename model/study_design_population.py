from typing import List
from pydantic import NonNegativeInt
from .api_base_model import ApiBaseModelWithIdAndDesc
from .code import Code

class StudyDesignPopulation(ApiBaseModelWithIdAndDesc):
  plannedNumberOfParticipants: NonNegativeInt
  plannedMaximumAgeOfParticipants: str  
  plannedMinimumAgeOfParticipants: str
  plannedSexOfParticipants: List[Code] = []
