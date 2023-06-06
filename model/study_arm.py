from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class StudyArm(ApiBaseModel):
  studyArmId: str
  studyArmName: str
  studyArmDescription: Union[str, None] = None
  studyArmType: Code
  studyArmDataOriginDescription: Union[str, None] = None
  studyArmDataOriginType: Code
