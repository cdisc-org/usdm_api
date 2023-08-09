from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameAndDesc
from .code import Code
from .endpoint import Endpoint

class Objective(ApiBaseModelWithIdNameAndDesc):
  objectiveLevel: Union[Code, None] = None
  objectiveEndpoints: List[Endpoint] = []