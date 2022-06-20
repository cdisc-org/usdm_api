from typing import Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class StudyData(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyDataName: str
  studyDataDesc: str
  crfLink: str
