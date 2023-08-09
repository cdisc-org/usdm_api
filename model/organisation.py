from typing import Union
from .api_base_model import ApiBaseModelWithIdAndName
from .code import Code
from .address import Address

class Organisation(ApiBaseModelWithIdAndName):
  organisationIdentifierScheme: str
  organisationIdentifier: str
  organisationType: Code
  organizationLegalAddress: Union[Address, None] = None
