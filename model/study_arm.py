from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class StudyArm(ApiBaseModel):
  uuid: Union[str, None] = None
  study_arm_desc: str
  study_arm_name: str
  study_arm_origin: Union[Code, str, None]
  study_arm_type: Union[Code, str, None]
  study_origin_type: Union[Code, str, None]
