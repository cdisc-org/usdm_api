from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from .transition_rule import TransitionRule
from uuid import UUID

class Encounter(ApiBaseModel):
  encounterId: str
  encounterName: str
  encounterDescription: str
  previousEncounterId: Union[str, None] = None
  nextEncounterId: Union[str, None] = None
  encounterType: Union[Code, None] = None
  encounterEnvironmentalSetting: Union[Code, None] = None
  encounterContactMode: Union[Code, None] = None
  transitionStartRule: Union[TransitionRule, None] = None
  transitionEndRule: Union[TransitionRule, None] = None
