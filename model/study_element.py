from typing import Union
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .transition_rule import TransitionRule

class StudyElement(ApiBaseModelWithIdNameAndDesc):
  transitionStartRule: Union[TransitionRule, None] = None
  transitionEndRule: Union[TransitionRule, None] = None
