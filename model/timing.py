from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from .scheduled_instance import ScheduledInstance

class Timing(ApiBaseModel):
  id: str = constr(min_length=1)
  timingType: Code
  timingValue: str
  timingDescription: Union[str, None] = None
  timingRelativeToFrom: Code
  relativeFromScheduledInstance: Union[ScheduledInstance, None] = None
  relativeToScheduledInstance: Union[ScheduledInstance, None] = None
  timingWindowLower: Union[str, None] = None
  timingWindowUpper: Union[str, None] = None
  timingWindow: Union[str, None] = None
