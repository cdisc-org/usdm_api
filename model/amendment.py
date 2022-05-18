from typing import Union
from .api_base_model import ApiBaseModel

class Amendment(ApiBaseModel):
  uuid: Union[str, None] = None
  amendment_effective_date: str
  amendment_version: str