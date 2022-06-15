from typing import List, Union
from .api_base_model import ApiBaseModel
from .procedure import Procedure
from .study_data import StudyData

from uuid import UUID

class Activity(ApiBaseModel):
  uuid: Union[UUID, None] = None
  activity_desc: str
  defined_procedure: Union[List[Procedure], List[UUID]] = []
  study_data_collection: Union[List[StudyData], List[UUID]] = []
