from pydantic import constr
from typing import List, Union
from .activity import Activity
from .api_base_model import ApiBaseModel
from .alias_code import AliasCode
from .code import Code
from .encounter import Encounter
from .study_cell import StudyCell
from .indication import Indication
from .investigational_intervention import InvestigationalIntervention
from .study_arm import StudyArm
from .study_epoch import StudyEpoch
from .study_element import StudyElement
from .study_design_population import StudyDesignPopulation
from .objective import Objective
from .schedule_timeline import ScheduleTimeline
from .estimand import Estimand

class StudyDesign(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  trialIntentTypes: List[Code] = []
  trialType: List[Code] = []
  interventionModel: Code
  studyCells: List[StudyCell]
  studyIndications: List[Indication] = []
  studyInvestigationalInterventions: List[InvestigationalIntervention] = []
  studyPopulations: List[StudyDesignPopulation] = []
  studyObjectives: List[Objective] = []
  studyScheduleTimelines: List[ScheduleTimeline] = []
  therapeuticAreas: List[Code] = []
  studyEstimands: List[Estimand] = []
  encounters: List[Encounter] = []
  activities: List[Activity] = []
  studyDesignRationale: str
  studyDesignBlindingScheme: Union[AliasCode, None] = None
  studyArms: List[StudyArm]
  studyEpochs: List[StudyEpoch]
  studyElements: List[StudyElement] = []
