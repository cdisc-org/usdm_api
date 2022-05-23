from pydantic import BaseModel
from uuid import uuid4
import json

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
    #print("Class:", self.__class__.__name__)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

  @classmethod
  def read(cls, uuid, store):
    return store.get(cls.__name__, uuid)

#  @classmethod
#  def read_full(cls, uuid, store):
#    return cls.read(uuid, store)

  @classmethod
  def read_full(cls, uuid, store):

    from .klass import Klass

    schema = cls.schema_json()
    instance = store.get(cls.__name__, uuid)
    x = json.loads(schema)
    for key, definition in x["properties"].items():
      print("READ_FULL 1: %s => %s" % (key, definition))
      if "anyOf" in definition:
        any_of = definition["anyOf"]
        print("READ_FULL 2: %s" % (any_of))
        for any_of_item in any_of:
          if "$ref" in any_of_item:
            print("READ_FULL 3: %s" % (any_of_item))
            klass_str = any_of_item["$ref"].replace("#/definitions/", "")
            klass = Klass.get(klass_str)
            if instance[key] != None:
              instance[key] = klass.read_full(instance[key], store)
          elif "items" in any_of_item:
            if "$ref" in any_of_item["items"]:
              print("READ_FULL 4: %s" % (any_of_item["items"]))
              print("READ_FULL 5: %s" % (key))
              print("READ_FULL 6: %s" % (instance[key]))
              klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
              klass = Klass.get(klass_str)
              result = []
              for item in instance[key]:
                result.append(klass.read_full(item, store))
              instance[key] = result
    return instance