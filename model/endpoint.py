from typing import Union
from .syntax_template_dictionary import SyntaxTemplateDictionary
from .code import Code

class Endpoint(SyntaxTemplateDictionary):
  purpose: str
  level: Union[Code, None] = None
