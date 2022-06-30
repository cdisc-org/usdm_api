from typing import Union
from .api_base_model import ApiBaseModel
from .activity import Activity
from .encounter import Encounter
from uuid import UUID

class WorkflowItem(ApiBaseModel):
  uuid: Union[UUID, None] = None
  workflowItemDesc: str
  previousWorkflowItemId: Union[UUID, None] = None
  nextWorkflowItemId: Union[UUID, None] = None
  workflowItemEncounter: Union[Encounter, UUID, None] = None
  workflowItemActivity: Union[Activity, UUID, None] = None