from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import StudyIdentifier
from .study_protocol import StudyProtocol
from .code import Code
from .study_design import StudyDesign
from uuid import uuid4

class Study(ApiBaseModel):
  uuid: Union[str, None] = None
  study_title: str
  study_version: str
  study_status: str
  study_protocol_version: str
  study_type: Union[Code, str, None]
  study_phase: Union[Code, str, None]
  study_identifier: Union[List[StudyIdentifier], List[str], None] = []
  study_protocol_reference: Union[StudyProtocol, str, None] = None
  study_design: Union[List[StudyDesign], List[str], None] = []

  def save(self, store):
    self.uuid = str(uuid4())
    self.study_type = self.check_and_save(self.study_type, store)
    self.study_phase = self.check_and_save(self.study_phase, store)
    self.study_protocol_reference = self.check_and_save(self.study_protocol_reference, store)
    if not self.study_identifier == None:
      for idx, identifier in enumerate(self.study_identifier):
        self.study_identifier[idx] = self.check_and_save(identifier, store)
    if not self.study_design == None:
      for idx, design in enumerate(self.study_design):
        print("STUDY DESIGN", design)
        self.study_design[idx] = self.check_and_save(design, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  # @classmethod
  # def read_full(cls, uuid, store):
  #   study = store.get(cls.__name__, uuid)
  #   study["study_type"] = Code.read_full(study["study_type"], store)
  #   study["study_phase"] = Code.read_full(study["study_phase"], store)
  #   if not study["study_identifier"] == None:
  #     for idx, identifier in enumerate(study["study_identifier"]):
  #       study["study_identifier"][idx] = StudyIdentifier.read_full(identifier, store)
  #   if not study["study_design"] == None:
  #     for idx, design in enumerate(study["study_design"]):
  #       study["study_design"][idx] =StudyDesign.read_full(design, store)
  #   return study
