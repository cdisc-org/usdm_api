from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class Timing(ApiBaseModel):
  timingId: str
  timingType: Code
  timingValue: str
  timingRelativeToFrom: Code
  timingWindow: Union[str, None] = None
  relativeFromScheduledInstanceId: Union[str, None] = None
  relativeToScheduledInstanceId: Union[str, None] = None
  timingDescription: str
  timingWindowLower: str
  timingWindowUpper: str