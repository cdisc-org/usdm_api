from typing import List, Union
from pydantic import Field
from .api_base_model import ApiBaseModel
from .study_protocol_document import StudyProtocolDocument
from .study_version import StudyVersion
from uuid import UUID

class Study(ApiBaseModel):
  id: Union[UUID, None] = None
  name: str = Field(min_length=1)
  description: str = ""
  label: str = ""
  versions: List[StudyVersion] = []
  documentedBy: Union[StudyProtocolDocument, None] = None
