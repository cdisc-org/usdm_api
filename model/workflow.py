from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .workflow_item import WorkflowItem
from uuid import UUID

class Workflow(ApiBaseModel):
  uuid: Union[UUID, None] = None
  workflowDesc: str
  workflowItems: Union[List[WorkflowItem], List[UUID], None]