from typing import Union, List, Literal
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .code import Code
from .study_design import StudyDesign
from .study_version import StudyVersion
from .masking import Masking
from .organization import Organization
from .assigned_person import AssignedPerson

class StudyRole(ApiBaseModelWithIdNameLabelAndDesc):
  code: Code
  appliesTo: Union[StudyDesign, StudyVersion]
  assignedPersons: List[AssignedPerson] = []
  organizations: List[Organization] = []
  masking: Union[Masking, None] = None
  instanceType: Literal['StudyRole']
