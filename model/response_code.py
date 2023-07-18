from pydantic import constr
from .api_base_model import ApiBaseModel
from .code import Code

class ResponseCode(ApiBaseModel):
  id: str = constr(min_length=1)
  responseCodeEnabled: bool
  code: Code
