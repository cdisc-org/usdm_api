from pydantic import constr
from typing import List, Dict, Union, Literal
from .api_base_model import ApiBaseModel
from .encounter import Encounter
from .timing import Timing

class ScheduledInstance(ApiBaseModel):
  id: str = constr(min_length=1)
  scheduledInstanceType: Literal['ACTIVITY', 'DECISION']
  scheduledInstanceTimings: List[Timing] = []
  scheduledInstanceTimelineId: Union[str, None] = None
  scheduleTimelineExitId: Union[str, None] = None
  defaultConditionId: Union[str, None] = None
  epochId: Union[str, None] = None

class ScheduledActivityInstance(ScheduledInstance):
  activityIds: List[str] = []
  scheduledActivityInstanceEncounter: Union[Encounter, None] = None

class ScheduledDecisionInstance(ScheduledInstance):
  conditionAssignments: Dict[str, str] = []
