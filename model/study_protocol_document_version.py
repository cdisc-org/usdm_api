from typing import List
from .api_base_model import ApiBaseModelWithId
from .code import Code

class StudyProtocolDocumentVersion(ApiBaseModelWithId):
  briefTitle: str
  officialTitle: str
  publicTitle: str
  scientificTitle: str
  protocolVersion: str
  protocolStatus: Code
  childrenId: List[str] = []