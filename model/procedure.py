from typing import Union
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class Procedure(ApiBaseModelWithIdNameAndDesc):
  procedureType: str
  procedureCode: Code
  procedureIsConditional: bool
  procedureIsConditionalReason: Union[str, None] = None
