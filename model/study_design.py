from typing import List, Union
from .code import Code
from .api_base_model import ApiBaseModel
from .study_cell import StudyCell
from .indication import Indication
from uuid import uuid4

class StudyDesign(ApiBaseModel):
  uuid: Union[str, None] = None
  trial_intent_type: Union[Code, str, None]
  trial_type: Union[Code, str, None]
  study_cell: Union[List[StudyCell], List[str], None] = []
  study_indication: Union[List[Indication], List[str], None] = []

  def save(self, store):
    self.uuid = str(uuid4())
    self.trial_intent_type = self.check_and_save(self.trial_intent_type, store)
    self.trial_type = self.check_and_save(self.trial_type, store)
    if not self.study_cell == None:
      for idx, cell in enumerate(self.study_cell):
        self.study_cell[idx] = self.check_and_save(cell, store)
    if not self.study_indication == None:
      for idx, indication in enumerate(self.study_indication):
        self.study_indication[idx] = self.check_and_save(indication, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  @classmethod
  def read_full(cls, uuid, store):
    study_design = store.get(cls.__name__, uuid)
    study_design["trial_type"] = Code.read_full(study_design["trial_type"], store)
    study_design["trial_intent_type"] = Code.read_full(study_design["trial_intent_type"], store)
    if not study_design["study_cell"] == None:
      for idx, cell in enumerate(study_design["study_cell"]):
        study_design["study_cell"][idx] = StudyCell.read_full(cell, store)
    if not study_design["study_indication"] == None:
      for idx, cell in enumerate(study_design["study_indication"]):
        study_design["study_indication"][idx] = Indication.read_full(cell, store)
    return study_design
