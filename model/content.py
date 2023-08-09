from typing import List
from .api_base_model import ApiBaseModelWithIdAndName

class Content(ApiBaseModelWithIdAndName):
  sectionNumber: str
  sectionTitle: str
  text: str
  contentChildren: List["Content"]
