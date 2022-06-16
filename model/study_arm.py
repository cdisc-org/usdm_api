from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class StudyArm(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyArmName: str
  studyArmDesc: str
  studyArmType: Union[Code, UUID]
  studyArmDataOriginDesc: str
  studyArmDataOriginType: Union[Code, UUID]
