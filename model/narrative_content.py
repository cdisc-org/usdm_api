from typing import List
from .api_base_model import ApiBaseModelWithIdAndName

class NarrativeContent(ApiBaseModelWithIdAndName):
  sectionNumber: str
  sectionTitle: str
  text: str = None
  contentChildIds: List[str] = []
