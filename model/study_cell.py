from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_arm import StudyArm
from .study_epoch import StudyEpoch
from .study_element import StudyElement
from uuid import UUID

class StudyCell(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_arm: Union[StudyArm, UUID, None]
  study_epoch: Union[StudyEpoch, UUID, None]
  study_element: Union[List[StudyElement], List[UUID], None] = []
