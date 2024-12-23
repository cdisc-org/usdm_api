from typing import List, Literal, Union
from .api_base_model import ApiBaseModelWithId
from .identifier import *
from .study_definition_document_version import *
from .alias_code import *
from .study_design import *
from .governance_date import GovernanceDate
from .study_amendment import StudyAmendment
from .study_title import StudyTitle
from .eligibility_criterion import EligibilityCriterion
from .narrative_content import NarrativeContentItem
from .comment_annotation import CommentAnnotation
from .abbreviation import Abbreviation
from .study_role import StudyRole
from .organization import Organization
from .administrable_product import AdministrableProduct
from .medical_device import MedicalDevice
from .product_organization_role import ProductOrganizationRole

class StudyVersion(ApiBaseModelWithId):
  versionIdentifier: str
  rationale: str
  documentVersionIds: List[str] = []
  dateValues: List[GovernanceDate] = []
  amendments: List[StudyAmendment] = []
  businessTherapeuticAreas: List[Code] = []
  studyIdentifiers: List[StudyIdentifier]
  referenceIdentifiers: List[ReferenceIdentifier] = []
  studyDesigns: List[Union[InterventionalStudyDesign, ObservationalStudyDesign]] = []
  titles: List[StudyTitle]
  criteria: List[EligibilityCriterion]
  narrativeContentItems: List[NarrativeContentItem] = []
  abbreviations: List[Abbreviation] = []
  roles: List[StudyRole] = []
  organizations: List[Organization] = []
  administrableProducts: List[AdministrableProduct] = []
  medicalDevices: List[MedicalDevice] = []
  productOrganizationRoles: List[ProductOrganizationRole] = []
  notes: List[CommentAnnotation] = []
  instanceType: Literal['StudyVersion']
