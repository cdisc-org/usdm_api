from typing import Union, List, Literal
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .organization import Organization

class AssignedPerson(ApiBaseModelWithIdNameLabelAndDesc):
  jobTitle: str
  organization: Union[Organization, None] = None
  instanceType: Literal['AssignedRole']
