from typing import List
from .api_base_model import ApiBaseModelWithIdAndName

class Content(ApiBaseModelWithIdAndName):
  sectionNumber: str
  sectionTitle: str
  text: str = None
  contentChildrenIds: List[str] = []
