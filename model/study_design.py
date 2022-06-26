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
  trialIntentType: Union[List[Code], List[UUID]]
  trialType: Union[Code, UUID]
  studyCells: Union[List[StudyCell], List[UUID], None] = []
  studyIndications: Union[List[Indication], List[UUID], None] = []
  studyInvestigationalInterventions: Union[List[InvestigationalIntervention], List[UUID], None] = []
  studyPopulations: Union[List[Population], List[UUID], None] = []
  studyObjectives: Union[List[Objective], List[UUID], None] = []
  studyWorkflows: Union[List[Workflow], List[UUID], None] = []

  @classmethod
  def search(cls, store, uuid):
    designs = store.get_by_klass_and_scope("StudyDesign", uuid)
    print("DESIGNS:", designs)
    return designs
