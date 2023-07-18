from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .alias_code import AliasCode

class BiomedicalConceptCategory(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  bcCategoryChildren: List["BiomedicalConceptCategory"] = []
  bcCategoryDescription: Union[str, None] = None
  bcCategoryMembers: List["BiomedicalConceptCategory"] = []
  bcCategoryCode: Union[AliasCode, None] = None
