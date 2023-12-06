from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc

class StudySite(ApiBaseModelWithIdNameLabelAndDesc):
  currentEnrollmentId: Union[str, None] = None
