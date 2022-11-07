from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class StudyArm(ApiBaseModel):
  studyArmId: str
  studyArmName: str
  studyArmDesc: str
  studyArmType: Union[Code, UUID]
  studyArmDataOriginDesc: str
  studyArmDataOriginType: Union[Code, UUID]
