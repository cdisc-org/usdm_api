from typing import Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class Activity(ApiBaseModel):
  uuid: Union[UUID, None] = None
  activity_desc: str
