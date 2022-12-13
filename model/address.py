from .api_base_model import ApiBaseModel

class Address(ApiBaseModel):

  text: str
  line: str
  city: str
  district: str
  state: str
  postalCode: str
  country: str
