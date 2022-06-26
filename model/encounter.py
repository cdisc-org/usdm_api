from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .transition_rule import TransitionRule
from .activity import Activity
from uuid import UUID

class Encounter(ApiBaseModel):
  uuid: Union[UUID, None] = None
  encounterName: str
  encounterDesc: str
  sequenceInStudy: int
  encounterType: Union[Code, UUID, None]
  encounterEnvironmentalSetting: Union[Code, UUID, None]
  encounterContactMode: Union[Code, UUID, None]
  activities: Union[List[Activity], List[UUID], None] = None
  transitionStartRule: Union[TransitionRule, UUID, None] = None
  transitionEndRule: Union[TransitionRule, UUID, None] = None
