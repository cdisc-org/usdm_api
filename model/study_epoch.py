from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .encounter import Encounter

from uuid import UUID

class StudyEpoch(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyEpochName: str
  studyEpochDesc: str
  previousStudyEpochId: Union[UUID, None] = None
  nextStudyEpochId: Union[UUID, None] = None
  studyEpochType: Union[Code, UUID]
  encounters: Union[List[Encounter], List[UUID]]
