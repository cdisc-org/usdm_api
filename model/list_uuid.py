from typing import List
from uuid import UUID
from .api_base_model import ApiBaseModel

class ListUUID(ApiBaseModel):
  uuid: List[UUID]

