from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from datetime import date
from .code import Code

class GovernanceDate(ApiBaseModelWithIdNameLabelAndDesc):
  type: Code
  dataValue: date 
