from typing import Union
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code

class Procedure(ApiBaseModelWithIdNameAndDesc):
  procedureDescription: Union[str, None] = None
  procedureCode: Code
  procedureIsConditional: bool
  procedureIsConditionalReason: Union[str, None] = None
