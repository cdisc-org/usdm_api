from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class StudyArm(ApiBaseModelWithIdNameAndDesc):
  studyArmType: Code
  studyArmDataOriginDescription: str
  studyArmDataOriginType: Code
