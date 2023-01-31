from typing import List, Union
from .api_base_model import ApiBaseModel
from .biomedical_concept import BiomedicalConcept
from .biomedical_concept_category import BiomedicalConceptCategory
from .biomedical_concept_surrogate import BiomedicalConceptSurrogate
from .procedure import Procedure
from .study_data import StudyData

from uuid import UUID

class Activity(ApiBaseModel):
  activityId: str
  activityName: str
  activityDescription: str
  previousActivityId: Union[str, None] = None
  nextActivityId: Union[str, None] = None
  definedProcedures: List[Procedure] = []
  studyDataCollection: List[StudyData] = []
  activityIsConditional: bool
  activityIsConditionalReason: str
  biomedicalConcept: BiomedicalConcept
  bcCategories: BiomedicalConceptCategory
  bcSurrogates: BiomedicalConceptSurrogate
