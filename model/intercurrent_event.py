from .api_base_model import ApiBaseModel
from typing import Union

class IntercurrentEvent(ApiBaseModel):
  intercurrentEventId: str
  intercurrentEventName: str
  intercurrentEventDescription: Union[str, None] = None
  intercurrentEventStrategy: str
