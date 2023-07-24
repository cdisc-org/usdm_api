from typing import List, Union
from .api_base_model import ApiBaseModelWithIdAndDesc
from .code import Code
from .endpoint import Endpoint

class Objective(ApiBaseModelWithIdAndDesc):
  objectiveLevel: Union[Code, None] = None
  objectiveEndpoints: List[Endpoint] = []