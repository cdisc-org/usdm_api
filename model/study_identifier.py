from .api_base_model import ApiBaseModelWithId
from .organisation import Organisation

class StudyIdentifier(ApiBaseModelWithId):
  studyIdentifier: str
  studyIdentifierScope: Organisation
