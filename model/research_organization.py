from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameAndLabel

class ResearchOrganization(ApiBaseModelWithIdNameAndLabel):
  identifier: str
  identifierScheme: str
  legalAddressId: Union[str, None] = None
  typeId: str
  managesIds: List[str]

