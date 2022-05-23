from typing import Union
from .api_base_model import ApiBaseModel
from .study_arm import StudyArm
from .study_epoch import StudyEpoch
from uuid import uuid4

class StudyCell(ApiBaseModel):
  uuid: Union[str, None] = None
  study_arm: Union[StudyArm, str, None]
  study_epoch: Union[StudyEpoch, str, None]

  def save(self, store):
    self.uuid = str(uuid4())
    if not self.study_arm == None:
      self.study_arm = self.check_and_save(self.study_arm, store)
    if not self.study_epoch == None:
      self.study_epoch = self.check_and_save(self.study_epoch, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
