from typing import List, Literal, Union
from .api_base_model import ApiBaseModelWithIdNameAndLabel
from .code import Code
from .address import Address

class Organization(ApiBaseModelWithIdNameAndLabel):
  organizationType: Code
  identifierScheme: str
  identifier: str
  legalAddress: Union[Address, None] = None
  instanceType: Literal['Organization']

class ResearchOrganization(Organization):
  manageIds: List[str]
  instanceType: Literal['ResearchOrganization']
