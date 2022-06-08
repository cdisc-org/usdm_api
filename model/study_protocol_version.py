from datetime import date
from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class StudyProtocolVersion(ApiBaseModel):
  uuid: Union[UUID, None]
  brief_title: str
  offical_title: str
  public_title: str
  scientific_title: str
  protocol_version: str
  protocol_amendment: Union[str, None] = None
  protocol_effective_date: date
  protocol_status: Union[UUID, Code]


