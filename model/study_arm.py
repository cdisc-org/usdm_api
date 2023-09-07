from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class StudyArm(ApiBaseModelWithIdNameAndDesc):
  type: Code
  studyArmDataOriginDescription: str
  dataOriginType: Code
