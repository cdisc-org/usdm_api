from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import uuid4

class StudyEpoch(ApiBaseModel):
  uuid: Union[str, None] = None
  study_epoch_desc: str
  study_epoch_name: str
  sequence_in_study: int
  epoch_type: Union[Code, str, None]