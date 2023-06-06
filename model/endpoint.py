from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class Endpoint(ApiBaseModel):
  endpointId: str
  endpointDescription: Union[str, None] = None
  endpointPurposeDescription: Union[str, None] = None
  endpointLevel: Union[Code, None] = None