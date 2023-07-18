from datetime import date
from pydantic import constr
from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code

class StudyProtocolVersion(ApiBaseModel):
  id: str = constr(min_length=1)
  briefTitle: str
  officialTitle: str
  publicTitle: str
  scientificTitle: str
  protocolVersion: str
  protocolAmendment: Union[str, None] = None
  protocolEffectiveDate: date
  protocolStatus: Code
