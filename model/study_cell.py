from pydantic import constr
from typing import List
from .api_base_model import ApiBaseModel
from .study_arm import StudyArm
from .study_element import StudyElement
from .study_epoch import StudyEpoch

class StudyCell(ApiBaseModel):
  id: str = constr(min_length=1)
  studyArm: StudyArm
  studyEpoch: StudyEpoch
  studyElement: List[StudyElement] = []
