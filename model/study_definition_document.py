from typing import List, Literal
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .study_definition_document_version import StudyDefinitionDocumentVersion

class StudyDefinitionDocument(ApiBaseModelWithIdNameLabelAndDesc):
  versions: List[StudyDefinitionDocumentVersion] = []
  instanceType: Literal['StudyDefinitionDocument']
