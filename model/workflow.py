from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .point_in_time import PointInTime

class Workflow(ApiBaseModel):
  uuid: Union[str, None] = None
  workflow_desc: str
  workflow_start_point: Union[PointInTime, str, None] = None
  workflow_end_point: Union[PointInTime, str, None] = None