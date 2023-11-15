from .api_base_model import ApiBaseModelWithId
from .code import Code

class Range(ApiBaseModelWithId):
  min: float
  max: float
  unit: Code
  