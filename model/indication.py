from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import UUID

class Indication(ApiBaseModel):
  uuid: Union[UUID, None] = None
  codes: Union[List[Code], List[UUID], None]
  indicationDesc: str
