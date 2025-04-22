from typing import List, Literal, Union
from pydantic import Field
from .api_base_model import ApiBaseModel
from .extension import ExtensionAttribute
from .study_definition_document import StudyDefinitionDocument
from .study_version import StudyVersion
from uuid import UUID

class Study(ApiBaseModel):
  id: Union[UUID, None] = None
  extensionAttributes: List[ExtensionAttribute] = []
  name: str = Field(min_length=1)
  description: Union[str, None] = None
  label: Union[str, None] = None
  versions: List[StudyVersion] = []
  documentedBy: List[StudyDefinitionDocument] = []
  instanceType: Literal['Study']
