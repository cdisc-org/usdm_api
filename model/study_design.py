from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .study_cell import StudyCell
from .indication import Indication
from .investigational_intervention import InvestigationalIntervention
from .population import Population
from .objective import Objective
from .workflow import Workflow
from uuid import UUID

class StudyDesign(ApiBaseModel):
  uuid: Union[UUID, None] = None
  trial_intent_type: Union[List[Code], List[UUID]]
  trial_type: Union[Code, UUID]
  study_cell: Union[List[StudyCell], List[UUID], None] = []
  study_indication: Union[List[Indication], List[UUID], None] = []
  study_investigational_interventions: Union[List[InvestigationalIntervention], List[UUID], None] = []
  study_population: Union[List[Population], List[UUID], None] = []
  study_objective: Union[List[Objective], List[UUID], None] = []
  study_workflow: Union[List[Workflow], List[UUID], None] = []