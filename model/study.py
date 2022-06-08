from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import *
from .study_protocol_version import *
from .code import *
from .study_design import *
from uuid import UUID

class Study(ApiBaseModel):
  uuid: Union[UUID, None]
  study_title: str
  study_version: str
  study_type: Union[Code, None]
  study_phase: Union[Code, None]
  study_identifier: Union[List[StudyIdentifier], List[UUID], None] = []
  study_protocol_version: Union[List[StudyProtocolVersion], List[UUID], None] = []
  study_design: Union[List[StudyDesign], List[UUID], None] = []

  @classmethod
  def scope_reuse(cls):
    return False

