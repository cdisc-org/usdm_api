from typing import List

from .api_base_model import ApiBaseModel
from .code import Code
from .condition import Condition
from .timing import Timing

class Timepoint(ApiBaseModel):
  timepointId: str
  timepointDescription: str
  timepointType: Code
  timepointCondition: Condition
  timepointExitId: str
  timepointScheduledAt: Timing
  previousTimepointIds: List[str] = []
  nextTimepointIds: List[str] = []
  timepointEncounterId: str
  timepointActivityIds: List[str] = []
  entryTimelineId: str
