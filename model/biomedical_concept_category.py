from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .alias_code import AliasCode

class BiomedicalConceptCategory(ApiBaseModelWithIdNameAndDesc):
  bcCategoryChildIds: List[str] = []
  bcCategoryDescription: Union[str, None] = None
  bcCategoryMemberIds: List[str] = []
  bcCategoryCode: Union[AliasCode, None] = None
