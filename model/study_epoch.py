from typing import Union
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class StudyEpoch(ApiBaseModelWithIdNameAndDesc):
  studyEpochType: Code
  previousStudyEpochId: Union[str, None] = None
  nextStudyEpochId: Union[str, None] = None
