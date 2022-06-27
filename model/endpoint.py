from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class Endpoint(ApiBaseModel):
  uuid: Union[UUID, None] = None
  endpointDesc: str
  endpointPurposeDesc: str
  endpointLevel: Union[Code, UUID, None]