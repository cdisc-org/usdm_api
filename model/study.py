from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import StudyIdentifier
from .study_protocol_version import StudyProtocolVersion
from .code import Code
from .study_design import StudyDesign
from uuid import UUID

class Study(ApiBaseModel):
  uuid: Union[UUID, None] = None
  study_title: str
  study_version: str
  study_status: str
  study_type: Union[Code, None]
  study_phase: Union[Code, None]
  study_identifier: Union[List[StudyIdentifier], List[UUID], None] = []
  study_protocol_version: Union[List[StudyProtocolVersion], List[UUID], None] = []
  study_design: Union[List[StudyDesign], List[UUID], None] = []

  @classmethod
  def scope_reuse(cls):
    return False

class StudyResponse(ApiBaseModel):
  uuid: UUID
  study_title: str
  study_version: str
  study_status: str
  study_type: Union[Code, None]
  study_phase: Union[Code, None]
  study_identifier: Union[List[StudyIdentifier], List[UUID], None] = []
  study_protocol_version: Union[List[StudyProtocolVersion], List[UUID], None] = []
  study_design: Union[List[StudyDesign], List[UUID], None] = []

