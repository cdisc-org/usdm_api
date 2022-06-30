from typing import List, Union
from .api_base_model import ApiBaseModel
from .procedure import Procedure
from .study_data import StudyData

from uuid import UUID

class Activity(ApiBaseModel):
  uuid: Union[UUID, None] = None
  activityName: str
  activityDesc: str
  previousActivityId: Union[UUID, None] = None
  nextActivityId: Union[UUID, None] = None
  definedProcedures: Union[List[Procedure], List[UUID]] = []
  studyDataCollection: Union[List[StudyData], List[UUID]] = []
