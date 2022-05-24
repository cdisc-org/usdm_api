from typing import Union
from .api_base_model import ApiBaseModel

class Activity(ApiBaseModel):
  uuid: Union[str, None] = None
  activity_desc: str
