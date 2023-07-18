from pydantic import constr
from typing import List
from .api_base_model import ApiBaseModel
from .code import Code

class AliasCode(ApiBaseModel):
  id: str = constr(min_length=1)
  standardCode: Code
  standardCodeAliases: List[Code] = []
