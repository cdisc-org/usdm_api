from typing import List

from .api_base_model import ApiBaseModel
from .exit import Exit
from .scheduled_instance import ScheduledInstance

class ScheduleTimeline(ApiBaseModel):
    scheduleTimelineId: str
    scheduleTimelineName: str
    scheduleTimelineDescription: str
    entryCondition: str
    entryScheduledInstanceId: str
    scheduleTimelineExits: List[Exit] = []
    scheduleTimelineIinstances: List[ScheduledInstance] = []