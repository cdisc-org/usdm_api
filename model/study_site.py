from typing import Literal, Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc

class StudySite(ApiBaseModelWithIdNameLabelAndDesc):
  currentEnrollmentId: Union[str, None] = None
  instanceType: Literal['StudySite'] = 'StudySite'
