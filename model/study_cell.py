from pydantic import constr
from typing import List
from .api_base_model import ApiBaseModel

class StudyCell(ApiBaseModel):
  id: str = constr(min_length=1)
  studyArmId: str
  studyEpochId: str
  studyElementIds: List[str] = []
