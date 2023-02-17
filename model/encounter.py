from typing import List, Union

from .api_base_model import ApiBaseModel
from .code import Code
from .condition import Condition
from .timing import Timing


class Encounter(ApiBaseModel):
  encounterId: str
  encounterName: str
  encounterDescription: str
  previousEncounterId: Union[str, None] = None
  nextEncounterId: Union[str, None] = None
  encounterType: Union[Code, None] = None
  encounterEnvironmentalSetting: Union[Code, None] = None
  encounterContactModes: List[Code] = []
  transitionStartRule: Union[Condition, None] = None
  transitionEndRule: Union[Condition, None] = None
  encounterScheduledAt: Union[Timing, None] = None
