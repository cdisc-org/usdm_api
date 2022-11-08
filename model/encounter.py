from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from .transition_rule import TransitionRule
from uuid import UUID

class Encounter(ApiBaseModel):
  encounterId: str
  encounterName: str
  encounterDesc: str
  previousEncounterId: Union[str, None] = None
  nextEncounterId: Union[str, None] = None
  encounterType: Union[Code, UUID, None] = None
  encounterEnvironmentalSetting: Union[Code, UUID, None] = None
  encounterContactMode: Union[Code, UUID, None] = None
  transitionStartRule: Union[TransitionRule, UUID, None] = None
  transitionEndRule: Union[TransitionRule, UUID, None] = None
