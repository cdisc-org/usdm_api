from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .study_cell import StudyCell
from .indication import Indication
from .investigational_intervention import InvestigationalIntervention
from .population import Population
from .objective import Objective
from .workflow import Workflow

class StudyDesign(ApiBaseModel):
  uuid: Union[str, None] = None
  trial_intent_type: Union[Code, str, None]
  trial_type: Union[Code, str, None]
  study_cell: Union[List[StudyCell], List[str], None] = []
  study_indication: Union[List[Indication], List[str], None] = []
  study_investigational_interventions: Union[List[InvestigationalIntervention], List[str], None] = []
  study_population: Union[List[Population], List[str], None] = []
  study_objective: Union[List[Objective], List[str], None] = []
  study_workflow: Union[List[Workflow], List[str], None] = []