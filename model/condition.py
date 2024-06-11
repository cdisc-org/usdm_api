from typing import List, Literal, Union
from .syntax_template import SyntaxTemplate

class Condition(SyntaxTemplate):
  text: str
  dictionaryId: Union[str, None] = None
  contextIds: List[str] = []
  appliesToIds: List[str] = []
  instanceType: Literal['Condition']
