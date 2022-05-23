from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from uuid import uuid4

class Indication(ApiBaseModel):
  uuid: Union[str, None] = None
  indication_desc: str
  indication: Union[List[Code], List[str], None]

  def save(self, store):
    self.uuid = str(uuid4())
    if not self.indication == None:
      for idx, design in enumerate(self.indication):
        self.indication[idx] = self.check_and_save(design, store)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  # @classmethod
  # def read_full(cls, uuid, store):
  #   study_indication = store.get(cls.__name__, uuid)
  #   if not study_indication["indication"] == None:
  #     for idx, indication in enumerate(study_indication["indication"]):
  #       study_indication["indication"][idx] = Code.read_full(indication, store)
  #   return study_indication