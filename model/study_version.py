from typing import List, Literal, Union
from .api_base_model import ApiBaseModelWithId
from .identifier import *
from .study_definition_document_version import *
from .alias_code import *
from .study_design import *
from .governance_date import GovernanceDate
from .study_amendment import StudyAmendment
from .study_title import StudyTitle
from .eligibility_criterion import EligibilityCriterionItem
from .narrative_content import NarrativeContentItem
from .comment_annotation import CommentAnnotation
from .abbreviation import Abbreviation
from .study_role import StudyRole
from .organization import Organization
from .administrable_product import AdministrableProduct
from .medical_device import MedicalDevice
from .product_organization_role import ProductOrganizationRole
from .biomedical_concept import BiomedicalConcept
from .biomedical_concept_category import BiomedicalConceptCategory
from .biomedical_concept_surrogate import BiomedicalConceptSurrogate
from .syntax_template_dictionary import SyntaxTemplateDictionary
from .condition import Condition

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
  eligibilityCriterionItems: List[EligibilityCriterionItem] = []
  narrativeContentItems: List[NarrativeContentItem] = []
  abbreviations: List[Abbreviation] = []
  roles: List[StudyRole] = []
  organizations: List[Organization] = []
  administrableProducts: List[AdministrableProduct] = []
  medicalDevices: List[MedicalDevice] = []
  productOrganizationRoles: List[ProductOrganizationRole] = []
  biomedicalConcepts: List[BiomedicalConcept] = []
  bcCategories: List[BiomedicalConceptCategory] = []
  bcSurrogates: List[BiomedicalConceptSurrogate] = []
  dictionaries: List[SyntaxTemplateDictionary] = []
  conditions: List[Condition] = []
  notes: List[CommentAnnotation] = []
  instanceType: Literal['StudyVersion']
