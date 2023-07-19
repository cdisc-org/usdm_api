from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .alias_code import AliasCode

class BiomedicalConceptCategory(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  bcCategoryChildIds: List[str] = []
  bcCategoryDescription: Union[str, None] = None
  bcCategoryMemberIds: List[str] = []
  bcCategoryCode: Union[AliasCode, None] = None
