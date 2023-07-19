from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .procedure import Procedure
from .schedule_timeline import ScheduleTimeline


class Activity(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  previousActivityId: Union[str, None] = None
  nextActivityId: Union[str, None] = None
  definedProcedures: List[Procedure] = []
  activityIsConditional: bool
  activityIsConditionalReason: Union[str, None] = None
  biomedicalConceptIds: List[str] = []
  bcCategoryIds: List[str] = []
  bcSurrogateIds: List[str] = []
  activityTimeline: Union[ScheduleTimeline, None] = None
