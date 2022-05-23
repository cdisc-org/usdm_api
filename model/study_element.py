from typing import Union
from .api_base_model import ApiBaseModel
from .rule import Rule
from uuid import uuid4

class StudyElement(ApiBaseModel):
  uuid: Union[str, None] = None
  study_element_desc: str
  study_element_name: str
  start_rule: Union[Rule, str, None] = None
  end_rule: Union[Rule, str, None] = None

  def save(self, store):
    self.uuid = str(uuid4())
    if not self.start_rule == None:
      self.start_rule = self.check_and_save(self.start_rule, store)
    if not self.end_rule == None:
      self.end_rule = self.check_and_save(self.end_rule, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  # @classmethod
  # def read_full(cls, uuid, store):
  #   study_element = store.get(cls.__name__, uuid)
  #   if not study_element["start_rule"] == None:
  #     study_element["start_rule"] = Rule.read_full(study_element["start_rule"], store)
  #   if not study_element["end_rule"] == None:
  #     study_element["end_rule"] = Rule.read_full(study_element["end_rule"], store)
  #   return study_element