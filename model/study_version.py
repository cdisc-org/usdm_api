from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import *
from .study_protocol_document_version import *
from .alias_code import *
from .code import Code as genericCode
from .study_design import *
from .governance_date import GovernanceDate
from uuid import UUID

class StudyVersion(ApiBaseModel):
  id: Union[UUID, None] = None
  studyTitle: str
  studyVersion: str
  approvedOn: GovernanceDate
  type: Union[genericCode, None] = None
  studyPhase: Union[AliasCode, None] = None
  businessTherapeuticAreas: List[Code] = []
  studyIdentifiers: List[StudyIdentifier] = []
  documentVersion: Union[StudyProtocolDocumentVersion, None] = None
  studyDesigns: List[StudyDesign] = []
  studyRationale: str
  studyAcronym: str
