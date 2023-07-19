from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class StudyEpoch(ApiBaseModel):
  id: str  = constr(min_length=1)
  name: str = constr(min_length=1)
  description: Union[str, None] = constr()
  studyEpochType: Code
  nextStudyEpoch: Union["StudyEpoch", None] = None
  previousStudyEpoch: Union["StudyEpoch", None] = None
