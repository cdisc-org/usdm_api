from typing import List, Union
from .syntax_template_dictionary import SyntaxTemplateDictionary
from .code import Code
from .endpoint import Endpoint

class Objective(SyntaxTemplateDictionary):
  level: Union[Code, None] = None
  objectiveEndpoints: List[Endpoint] = []