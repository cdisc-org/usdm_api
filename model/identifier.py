from typing import Literal
from .api_base_model import ApiBaseModelWithId
from .organization import Organization

class Identifier(ApiBaseModelWithId):
  text: str
  scope: Organization
  instanceType: Literal['Identifier']
