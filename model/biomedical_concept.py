from typing import List
from .api_base_model import ApiBaseModel
from .biomedical_concept_property import BiomedicalConceptProperty

class BiomedicalConcept(ApiBaseModel):
  biomedicalConceptId: str
  bcName: str
  bcSynonyms: List[str] = []
  bcReference: str
  bcProperties: List[BiomedicalConceptProperty] = []
