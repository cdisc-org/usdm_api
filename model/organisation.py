from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel
from .code import Code

class Organisation(ApiBaseModel):
  uuid: Union[UUID, None] = None
  organisation_identifier_scheme: str
  organisation_identifier: str
  organisation_name: str
  organisation_type: Code

class OrganisationResponse(ApiBaseModel):
  uuid: UUID
  organisation_identifier_scheme: str
  organisation_identifier: str
  organisation_name: str
  organisation_type: UUID
