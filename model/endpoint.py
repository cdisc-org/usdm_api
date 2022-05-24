from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class Endpoint(ApiBaseModel):
  uuid: Union[str, None] = None
  endpoint_desc: str
  endpoint_purpose: Union[Code, str, None]
  outcome_level: Union[Code, str, None]