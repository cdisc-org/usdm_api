from typing import Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .code import Code
from .study_intervention import StudyIntervention

class Procedure(ApiBaseModelWithIdNameLabelAndDesc):
  procedureType: str
  code: Code
  studyInterventionId: Union[str, None] = None
