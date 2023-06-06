from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code

class Indication(ApiBaseModel):
  indicationId: str
  indicationDescription: Union[str, None] = None
  codes: List[Code] = []
