from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .analysis_population import AnalysisPopulation
from .investigational_intervention import InvestigationalIntervention
from .endpoint import Endpoint
from .intercurrent_event import IntercurrentEvent
from uuid import UUID

class Estimand(ApiBaseModel):
  id: str = constr(min_length=1)
  summaryMeasure: str
  analysisPopulation: AnalysisPopulation
  treatment: Union[str, None] = None
  variableOfInterest: Union[str, None] = None
  intercurrentEvents: List[IntercurrentEvent] = []
