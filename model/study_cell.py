from typing import List
from .api_base_model import ApiBaseModel
from .study_element import StudyElement

class StudyCell(ApiBaseModel):
  studyCellId: str
  studyArmId: str
  studyEpochId: str
  studyElements: List[StudyElement] = []
