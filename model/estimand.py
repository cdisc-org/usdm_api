from typing import List, Union
from .api_base_model import ApiBaseModel
from .analysis_population import AnalysisPopulation
from .investigational_intervention import InvestigationalIntervention
from .endpoint import Endpoint
from .intercurrent_event import IntercurrentEvent
from uuid import UUID

class Estimand(ApiBaseModel):
  estimandId: str
  summaryMeasure: str
  analysisPopulation: Union[AnalysisPopulation, UUID]
  treatment: Union[InvestigationalIntervention, UUID]
  variableOfInterest: Union[Endpoint, UUID]
  intercurrentEvents: Union[List[IntercurrentEvent], List[UUID]]
