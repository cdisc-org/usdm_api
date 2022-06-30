from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class IntercurrentEvent(ApiBaseModel):
  uuid: Union[UUID, None] = None
  intercurrentEventName: str
  intercurrentEventDesc: str
  intercurrentEventStrategy: str
