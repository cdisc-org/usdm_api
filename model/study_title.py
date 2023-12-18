from typing import Literal
from .api_base_model import ApiBaseModelWithId

class StudyTitle(ApiBaseModelWithId):
  text: str
  typeId: str
  instanceType: Literal['StudyTitle'] = 'StudyTitle'
