from pydantic import constr
from typing import List
from .api_base_model import ApiBaseModelWithId
from .code import Code

class AliasCode(ApiBaseModelWithId):
  id: str = constr(min_length=1)
  standardCode: Code
  standardCodeAliases: List[Code] = []
