from typing import List
from .api_base_model import ApiBaseModel
from .biomedical_concept import BiomedicalConcept

class BiomedicalConceptCategory(ApiBaseModel):
  biomedicalConceptCategoryId: str
  bcCategoryParents: List["BiomedicalConceptCategory"] = []
  bcCategoryChildren: List["BiomedicalConceptCategory"] = []
  bcCategoryName: str
  bcCategoryDescription: str
  bcCategoryMembers: List[BiomedicalConcept] = []
