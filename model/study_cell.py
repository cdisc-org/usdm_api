from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_arm import StudyArm
from .study_epoch import StudyEpoch
from .study_element import StudyElement
from uuid import uuid4

class StudyCell(ApiBaseModel):
  uuid: Union[str, None] = None
  study_arm: Union[StudyArm, str, None]
  study_epoch: Union[StudyEpoch, str, None]
  study_element: Union[List[StudyElement], List[str], None] = []

  def save(self, store):
    self.uuid = str(uuid4())
    if not self.study_arm == None:
      self.study_arm = self.check_and_save(self.study_arm, store)
    if not self.study_epoch == None:
      self.study_epoch = self.check_and_save(self.study_epoch, store)
    if not self.study_element == None:
      for idx, design in enumerate(self.study_element):
        self.study_element[idx] = self.check_and_save(design, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  # @classmethod
  # def read_full(cls, uuid, store):
  #   study_cell = store.get(cls.__name__, uuid)
  #   if not study_cell["study_arm"] == None:
  #     study_cell["study_arm"] = StudyArm.read_full(study_cell["study_arm"], store)
  #   if not study_cell["study_epoch"] == None:
  #     study_cell["study_epoch"] = StudyEpoch.read_full(study_cell["study_epoch"], store)
  #   if not study_cell["study_element"] == None:
  #     for idx, design in enumerate(study_cell["study_element"]):
  #       study_cell["study_element"][idx] = StudyElement.read_full(design, store)
  #   return study_cell