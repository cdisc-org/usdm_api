from msilib import sequence
from typing import List, Union
from .api_base_model import ApiBaseModel
from .transition_rule import TransitionRule
from .encounter import Encounter
from .activity import Activity

from uuid import UUID

class StudyElement(ApiBaseModel):
  uuid: Union[UUID, None] = None
  studyElementName: str
  studyElementDesc: str
  encounters: Union[List[Encounter], List[UUID], None] = []
  activities: Union[List[Activity], List[UUID], None] = []
  transitionStartRule: Union[TransitionRule, UUID, None] = None
  transitionEndRule: Union[TransitionRule, UUID, None] = None
