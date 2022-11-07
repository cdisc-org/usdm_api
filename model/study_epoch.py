from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .encounter import Encounter

from uuid import UUID

class StudyEpoch(ApiBaseModel):
  studyEpochId: str
  studyEpochName: str
  studyEpochDesc: str
  studyEpochType: Union[Code, UUID]
  previousStudyEpochId: str
  nextStudyEpochId: str
  encounters: Union[List[Encounter], List[UUID]]
