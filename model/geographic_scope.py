from .api_base_model import ApiBaseModelWithId
from .code import Code
from .alias_code import AliasCode

class GeographicScope(ApiBaseModelWithId):
  type: Code
  code: AliasCode
