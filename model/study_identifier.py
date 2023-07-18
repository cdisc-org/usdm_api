from pydantic import constr
from .api_base_model import ApiBaseModel
from .organisation import Organisation

class StudyIdentifier(ApiBaseModel):
  id: str = constr(min_length=1)
  studyIdentifier: str
  studyIdentifierScope: Organisation
