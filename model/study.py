from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import *
from .study_protocol_version import *
from .code import *
from .study_design import *
from uuid import UUID

class Study(ApiBaseModel):
  uuid: Union[UUID, None]
  studyTitle: str
  studyVersion: str
  studyType: Union[Code, None]
  studyPhase: Union[Code, None]
  studyIdentifiers: Union[List[StudyIdentifier], List[UUID], None] = []
  studyProtocolVersions: Union[List[StudyProtocolVersion], List[UUID], None] = []
  studyDesigns: Union[List[StudyDesign], List[UUID], None] = []

  @classmethod
  def scope_reuse(cls):
    return False

