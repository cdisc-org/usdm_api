from typing import List

from .api_base_model import ApiBaseModel
from .condition import Condition
# from .exit import Exit
from .timepoint import Timepoint

class Timeline(ApiBaseModel):
    timelineId: str
    timelineDescription: str
    entryCondition: Condition
    entryTimepointId: str
    # Exit not yet defined
    # private Exit timelineExit;
    timelineTimepoints: List[Timepoint] = []