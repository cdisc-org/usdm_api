from typing import Literal, Union
from .api_base_model import ApiBaseModelWithId
from .syntax_template import SyntaxTemplate
from .code import Code

class EligibilityCriterion(ApiBaseModelWithId):
  category: Code
  identifier: str
  criterionItemId: str
  nextId: Union[str, None] = None
  previousId: Union[str, None] = None
  instanceType: Literal['EligibilityCriterion']

class EligibilityCriterionItem(SyntaxTemplate):
  instanceType: Literal['EligibilityCriterionItem']
