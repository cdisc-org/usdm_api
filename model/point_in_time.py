from datetime import date
from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class PointInTime(ApiBaseModel):
  uuid: Union[str, None] = None
  start_date: date
  end_date: date
  point_in_time_type: Union[Code, str, None]
