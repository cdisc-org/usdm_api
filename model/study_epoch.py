from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class StudyEpoch(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_epoch_name: str
  study_epoch_desc: str
  epoch_type: Union[Code, UUID]
  sequence_in_study: int
