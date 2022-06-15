from typing import Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class StudyData(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_data_name: str
  study_data_desc: str
  crf_link: str
