from typing import List
from .api_base_model import ApiBaseModel

class BiomedicalConceptCategory(ApiBaseModel):
  biomedicalConceptCategoryId: str
  bcCategoryParents: List[str] = []
  bcCategoryChildren: List[str] = []
  bcCategoryName: str
  bcCategoryDescription: str
  bcCategoryMemberIds: List[str] = []
