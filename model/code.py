from pydantic import constr
from .api_base_model import ApiBaseModel

class Code(ApiBaseModel):
  id: str = constr(min_length=1)
  code: str
  codeSystem: str
  codeSystemVersion: str
  decode: str
