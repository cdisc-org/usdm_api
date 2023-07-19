from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .schedule_timeline_exit import ScheduleTimelineExit
from .scheduled_instance import ScheduledInstance

class ScheduleTimeline(ApiBaseModel):
  mainTimeline: bool
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  entryCondition: str
  scheduleTimelineEntryId: Union[str, None] = None
  scheduleTimelineExits: List[ScheduleTimelineExit] = []
  scheduleTimelineInstances: List[ScheduledInstance] = []