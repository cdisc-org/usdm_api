from typing import Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .quantity import Quantity
from .administration_duration import AdministrationDuration
from .alias_code import AliasCode
from typing import Literal

class AgentAdministration(ApiBaseModelWithIdNameLabelAndDesc):
  duration:	AdministrationDuration
  dose:	Quantity
  route:	AliasCode
  frequency:	AliasCode
  instanceType: Literal['AgentAdministration']
