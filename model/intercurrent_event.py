from .api_base_model import ApiBaseModel

class IntercurrentEvent(ApiBaseModel):
  intercurrentEventId: str
  intercurrentEventName: str
  intercurrentEventDesc: str
  intercurrentEventStrategy: str
