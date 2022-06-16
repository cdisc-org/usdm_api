from typing import Union
from uuid import UUID
from .api_base_model import ApiBaseModel
from .code import Code

class Organisation(ApiBaseModel):
  uuid: Union[UUID, None]
  organisationIdentifierScheme: str
  organisationIdentifier: str
  organisationName: str
  organisationType: Union[UUID, Code]

  @classmethod
  def global_reuse(cls):
    return True

