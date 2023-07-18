from pydantic import constr
from .api_base_model import ApiBaseModel

class ScheduleTimelineExit(ApiBaseModel):
  id: str = constr(min_length=1)\
