from pydantic import constr
from typing import List
from .alias_code import AliasCode
from .api_base_model import ApiBaseModel
from .response_code import ResponseCode

class BiomedicalConceptProperty(ApiBaseModel):
  id: str = constr(min_length=1)
  bcPropertyName: str
  bcPropertyRequired: bool
  bcPropertyEnabled: bool
  bcPropertyDatatype: str
  bcPropertyResponseCodes: List[ResponseCode] = []
  bcPropertyConceptCode: AliasCode
