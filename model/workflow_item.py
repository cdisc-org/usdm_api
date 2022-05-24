from datetime import date
from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .point_in_time import PointInTime
from .activity import Activity
from .encounter import Encounter

class WorkflowItem(ApiBaseModel):
  uuid: Union[str, None] = None
  description: str
  from_point_in_time: Union[PointInTime, str, None] = None
  to_point_in_time: Union[PointInTime, str, None] = None
  previous_workflow_item: Union[str, None] = None
  encounter: Union[Encounter, str, None] = None
  activity: Union[Activity, str, None] = None