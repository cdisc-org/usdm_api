from typing import List, Union
from .api_base_model import ApiBaseModel
from .transition_rule import TransitionRule
from .encounter import Encounter

from uuid import UUID

class StudyElement(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyElementName: str
  studyElementDesc: str
  encounters: Union[List[Encounter], List[UUID], None] = []
  transitionStartRule: Union[TransitionRule, UUID, None] = None
  transitionEndRule: Union[TransitionRule, UUID, None] = None
