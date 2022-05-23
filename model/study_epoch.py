from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import uuid4

class StudyEpoch(ApiBaseModel):
  uuid: Union[str, None] = None
  study_epoch_desc: str
  study_epoch_name: str
  sequence_in_study: int
  epoch_type: Union[Code, str, None]

  def save(self, store):
    self.uuid = str(uuid4())
    if not self.epoch_type == None:
      self.epoch_type = self.check_and_save(self.epoch_type, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  @classmethod
  def read_full(cls, uuid, store):
    study_epoch = store.get(cls.__name__, uuid)
    study_epoch["epoch_type"] = Code.read_full(study_epoch["epoch_type"], store)
    return study_epoch