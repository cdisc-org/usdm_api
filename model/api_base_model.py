from pydantic import BaseModel
from uuid import uuid4

class ApiBaseModel(BaseModel):

  def check_and_save(self, item, store):
    if item == None:
      return None
    elif isinstance(item, str):
      return item
    else:
      return item.save(store)

  def save(self, store):
    self.uuid = str(uuid4())
    print("Class:", self.__class__.__name__)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  @classmethod
  def read(cls, uuid, store):
    print("NAME:", cls.__name__)
    return store.get(cls.__name__, uuid)