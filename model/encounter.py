from pydantic import constr
from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .timing import Timing
from .transition_rule import TransitionRule

class Encounter(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  previousEncounter: Union["Encounter", None] = None
  nextEncounter: Union["Encounter", None] = None
  encounterType: Union[Code, None] = None
  encounterEnvironmentalSetting: Union[Code, None] = None
  encounterContactModes: List[Code] = []
  transitionStartRule: Union[TransitionRule, None] = None
  transitionEndRule: Union[TransitionRule, None] = None
