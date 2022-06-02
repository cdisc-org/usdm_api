from typing import List, Union
from .api_base_model import ApiBaseModel
from .amendment import Amendment
from uuid import uuid4

class StudyProtocol(ApiBaseModel):
  uuid: Union[str, None] = None
  brief_title: str
  full_title: str
  public_title: str
  scientific_title: str
  version: str
  study_protocol_amendments: Union[List[Amendment], List[str], None] = []
