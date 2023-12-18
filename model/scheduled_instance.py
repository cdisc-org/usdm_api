from typing import List, Literal, Dict, Union
from .api_base_model import ApiBaseModelWithId
from .timing import Timing

class ScheduledInstance(ApiBaseModelWithId):
  timings: List[Timing] = []
  timelineId: Union[str, None] = None
  timelineExitId: Union[str, None] = None
  defaultConditionId: Union[str, None] = None
  epochId: Union[str, None] = None
  instanceType: Literal['ScheduledInstance'] = 'ScheduledInstance'

class ScheduledActivityInstance(ScheduledInstance):
  activityIds: List[str] = []
  encounterId: Union[str, None] = None
  instanceType: Literal['ScheduledActivityInstance'] = 'ScheduledActivityInstance'

class ScheduledDecisionInstance(ScheduledInstance):
  conditionAssignments: Dict[str, str]
  instanceType: Literal['ScheduledDecisionInstance'] = 'ScheduledDecisionInstance'
