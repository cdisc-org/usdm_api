from typing import Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import uuid4

class StudyArm(ApiBaseModel):
  uuid: Union[str, None] = None
  study_arm_desc: str
  study_arm_name: str
  study_arm_origin: Union[Code, str, None]
  study_arm_type: Union[Code, str, None]
  study_origin_type: Union[Code, str, None]

  def save(self, store):
    self.uuid = str(uuid4())
    if not self.study_arm_origin == None:
      self.study_arm_origin = self.check_and_save(self.study_arm_origin, store)
    if not self.study_arm_type == None:
      self.study_arm_type = self.check_and_save(self.study_arm_type, store)
    if not self.study_origin_type == None:
      self.study_origin_type = self.check_and_save(self.study_origin_type, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  # @classmethod
  # def read_full(cls, uuid, store):
  #   study_arm = store.get(cls.__name__, uuid)
  #   study_arm["study_arm_type"] = Code.read_full(study_arm["study_arm_type"], store)
  #   study_arm["study_arm_origin"] = Code.read_full(study_arm["study_arm_origin"], store)
  #   study_arm["study_origin_type"] = Code.read_full(study_arm["study_origin_type"], store)
  #   return study_arm