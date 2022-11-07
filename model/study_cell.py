from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_arm import StudyArm
from .study_epoch import StudyEpoch
from .study_element import StudyElement
from uuid import UUID

class StudyCell(ApiBaseModel):
  studyCellId: str
  studyArm: Union[StudyArm, UUID, None]
  studyEpoch: Union[StudyEpoch, UUID, None]
  studyElements: Union[List[StudyElement], List[UUID], None] = []
