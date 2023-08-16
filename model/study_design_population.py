from typing import List
from pydantic import NonNegativeInt
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class StudyDesignPopulation(ApiBaseModelWithIdNameAndDesc):
  plannedNumberOfParticipants: NonNegativeInt
  plannedMaximumAgeOfParticipants: str  
  plannedMinimumAgeOfParticipants: str
  plannedSexOfParticipants: List[Code] = []
