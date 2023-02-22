from typing import List

from .api_base_model import ApiBaseModel
from .timing import Timing

class ScheduledInstance(ApiBaseModel):
    scheduledInstanceId: str
    scheduleSequenceNumber: int
    scheduleTimelineExitId: str
    scheduledInstanceEncounterId: str
    secheduledInstanceTimingIds: List[str] = []

class ScheduledActivityInstance(ScheduledInstance):
    activityIds: List[str] = []

class ScheduledDecisionInstance(ScheduledInstance):
    booleanCondition: str
    trueTimingId: str
    falseTimingId: str
    conditions: List[str] = []
    conditionTimings: List[Timing] = []