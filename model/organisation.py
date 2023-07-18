from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from .address import Address

class Organisation(ApiBaseModel):
  id: str = constr(min_length=1)
  organisationName: str = constr(min_length=1)
  organisationIdentifierScheme: str
  organisationIdentifier: str
  organisationType: Code
  organizationLegalAddress: Union[Address, None] = None
