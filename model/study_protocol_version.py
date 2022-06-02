from datetime import date
from typing import List, Union
from .api_base_model import ApiBaseModel
from uuid import UUID

class StudyProtocolVersion(ApiBaseModel):
  uuid: Union[UUID, None] = None
  brief_title: str
  offical_title: str
  public_title: str
  scientific_title: str
  version: str
  amendment: Union[str, None] = None
  effective_date: date

class StudyProtocolVersionResponse(ApiBaseModel):
  uuid: UUID
  brief_title: str
  offical_title: str
  public_title: str
  scientific_title: str
  version: str
  amendment: Union[str, None] = None
  effective_date: date