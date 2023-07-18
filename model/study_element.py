from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .transition_rule import TransitionRule

class StudyElement(ApiBaseModel):
  id: str = constr(min_length=1)
  name: str = constr(min_length=1)
  description: str = constr()
  transitionStartRule: Union[TransitionRule, None] = None
  transitionEndRule: Union[TransitionRule, None] = None
