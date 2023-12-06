from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameAndLabel

class OversightCommittee(ApiBaseModelWithIdNameAndLabel):
  identifier: str
  identifierScheme: str
  legalAddressId: Union[str, None] = None
  typeId: str
  overseesIds: List[str]
