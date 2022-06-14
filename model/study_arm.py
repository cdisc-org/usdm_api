from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class StudyArm(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_arm_name: str
  study_arm_desc: str
  study_arm_type: Union[Code, UUID]
  study_arm_data_origin_desc: str
  study_arm_data_origin_type: Union[Code, UUID]
