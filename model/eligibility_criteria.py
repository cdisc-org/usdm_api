from typing import List, Union
from .syntax_template_dictionary import SyntaxTemplateDictionary
from .code import Code

class EligibilityCriteria(SyntaxTemplateDictionary):
  category: Union[Code, None] = None
  identifier: str
  nextCriterion: List["EligibilityCriteria"] = []
  previousCriterion: List["EligibilityCriteria"] = []