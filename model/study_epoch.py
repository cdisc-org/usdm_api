from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class StudyEpoch(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyEpochName: str
  studyEpochDesc: str
  studyEpochType: Union[Code, UUID]
  sequenceInStudyDesign: int
