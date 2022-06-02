from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import StudyIdentifier
from .study_protocol import StudyProtocol
from .code import Code
from .study_design import StudyDesign
from uuid import uuid4

class Study(ApiBaseModel):
  uuid: Union[str, None] = None
  study_title: str
  study_version: str
  study_status: str
  study_protocol_version: str
  study_type: Union[Code, str, None]
  study_phase: Union[Code, str, None]
  study_identifier: Union[List[StudyIdentifier], List[str], None] = []
  study_protocol_reference: Union[StudyProtocol, str, None] = None
  study_design: Union[List[StudyDesign], List[str], None] = []
