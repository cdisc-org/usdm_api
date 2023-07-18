from pydantic import constr
from typing import List, Dict, Union, Literal
from .activity import Activity
from .api_base_model import ApiBaseModel
from encounter import Encounter
from .schedule_timeline import ScheduleTimeline
from .schedule_timeline_exit import ScheduleTimelineExit
from .study_epoch import StudyEpoch
from .timing import Timing

class ScheduledInstance(ApiBaseModel):
  id: str = constr(min_length=1)
  scheduledInstanceType: Literal['ACTIVITY', 'DECISION']
  scheduledInstanceTimings: List[Timing] = []
  scheduledInstanceTimeline: Union[ScheduleTimeline, None] = None
  scheduleTimelineExit: Union[ScheduleTimelineExit, None] = None
  defaultCondition: Union["ScheduledInstance", None] = None
  epoch: Union[StudyEpoch, None] = None

class ScheduledActivityInstance(ScheduledInstance):
  activity: List[Activity] = []
  scheduledActivityInstanceEncounter: Union[Encounter, None] = None

class ScheduledDecisionInstance(ScheduledInstance):
  conditionAssignments: Dict[str, str] = []