from typing import List, Literal
from .api_base_model import ApiBaseModelWithId
from .comment_annotation import CommentAnnotation

class Abbreviation(ApiBaseModelWithId):
  abbreviation: str
  lomgName: str
  notes: List[CommentAnnotation] = []
  instanceType: Literal['Address']
