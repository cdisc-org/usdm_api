from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .biomedical_concept import BiomedicalConcept
from .biomedical_concept_category import BiomedicalConceptCategory
from .biomedical_concept_surrogate import BiomedicalConceptSurrogate
from .procedure import Procedure
from .schedule_timeline import ScheduleTimeline


class Activity(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  previousActivity: Union["Activity", None] = None
  nextActivity: Union["Activity", None] = None
  definedProcedures: List[Procedure] = []
  activityIsConditional: bool
  activityIsConditionalReason: Union[str, None] = None
  biomedicalConcepts: List[BiomedicalConcept] = []
  bcCategories: List[BiomedicalConceptCategory] = []
  bcSurrogates: List[BiomedicalConceptSurrogate] = []
  activityTimeline: Union[ScheduleTimeline, None] = None
