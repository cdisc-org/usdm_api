from typing import List, Union
from .api_base_model import ApiBaseModel
from .amendment import Amendment
from uuid import uuid4

class StudyProtocol(ApiBaseModel):
  uuid: Union[str, None] = None
  brief_title: str
  full_title: str
  public_title: str
  scientific_title: str
  version: str
  study_protocol_amendments: Union[List[Amendment], List[str], None] = []

  def save(self, store):
    self.uuid = str(uuid4())
    for idx, amendment in enumerate(self.study_protocol_amendments, store):
      self.study_protocol_amendments[idx] = self.check_and_save(amendment, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid
