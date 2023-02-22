from typing import List

from .api_base_model import ApiBaseModel
from .schedule_timeline_exit import ScheduleTimelineExit
from .scheduled_instance import ScheduledInstance

class ScheduleTimeline(ApiBaseModel):
    scheduleTimelineId: str
    scheduleTimelineName: str
    scheduleTimelineDescription: str
    entryCondition: str
    entryScheduledInstanceId: str
    scheduleTimelineScheduleTimelineExits: List[ScheduleTimelineExit] = []
    scheduleTimelineInstances: List[ScheduledInstance] = []