from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_arm import StudyArm
from .study_epoch import StudyEpoch
from .study_element import StudyElement
from uuid import uuid4

class StudyCell(ApiBaseModel):
  uuid: Union[str, None] = None
  study_arm: Union[StudyArm, str, None]
  study_epoch: Union[StudyEpoch, str, None]
  study_element: Union[List[StudyElement], List[str], None] = []
