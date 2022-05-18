from typing import Union
from .api_base_model import ApiBaseModel

class StudyIdentifier(ApiBaseModel):
  uuid: Union[str, None] = None
  study_identifier_desc: str
  study_identifier_name: str
  org_code: str