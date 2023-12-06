from typing import List, Union
from .api_base_model import ApiBaseModelWithId

class StudyTitle(ApiBaseModelWithId):
  text: str
  typeId: str
