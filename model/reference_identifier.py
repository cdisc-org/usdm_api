from typing import Literal
from .identifier import Identifier
from .code import Code

class ReferenceIdentifier(Identifier):
  type: Code
  instanceType: Literal['ReferenceIdentifier']
