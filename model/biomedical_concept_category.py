from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .alias_code import AliasCode

class BiomedicalConceptCategory(ApiBaseModelWithIdNameLabelAndDesc):
  ChildrenIds: List[str] = []
  MemberIds: List[str] = []
  code: Union[AliasCode, None] = None
