from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .comment_annotation import CommentAnnotation

class SyntaxTemplate(ApiBaseModelWithIdNameLabelAndDesc):
  text: str
  dictionaryId: Union[str, None] = None
  notes: List[CommentAnnotation] = []
