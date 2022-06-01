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
    print("READ:", uuid)
    print("READ:", cls.__name__)
    return store.get(cls.__name__, uuid)

  def recursive_save(self, store):

    from .klass import Klass

    schema = self.__class__.schema_json()
    x = json.loads(schema)
    self.uuid = str(uuid4())
    for key, definition in x["properties"].items():
      #print("RECURSIVE_SAVE 1: %s => %s" % (key, definition))
      if "anyOf" in definition:
        any_of = definition["anyOf"]
        #print("RECURSIVE_SAVE 2: %s" % (any_of))
        for any_of_item in any_of:
          if "$ref" in any_of_item:
            klass_str = any_of_item["$ref"].replace("#/definitions/", "")
            klass = Klass.get(klass_str)
            if getattr(self, key) != None:
              setattr(self, key, klass.recursive_save(getattr(self, key), store)) 
          elif "items" in any_of_item:
            if "$ref" in any_of_item["items"]:
              klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
              klass = Klass.get(klass_str)
              result = []
              for item in getattr(self, key):
                result.append(klass.recursive_save(item, store))
              setattr(self, key, result)
      elif "$ref" in definition:
        klass_str = definition["$ref"].replace("#/definitions/", "")
        klass = Klass.get(klass_str)
        if getattr(self, key) != None:
          setattr(self, key, klass.recursive_save(getattr(self, key), store)) 
    self.save(store)
    return self.uuid

  @classmethod
  def recursive_read(cls, uuid, store):

    from .klass import Klass

    schema = cls.schema_json()
    instance = store.get(cls.__name__, uuid)
    x = json.loads(schema)
    for key, definition in x["properties"].items():
      #print("RECURSIVE_READ 1: %s => %s" % (key, definition))
      if "anyOf" in definition:
        any_of = definition["anyOf"]
        #print("RECURSIVE_READ 2: %s" % (any_of))
        for any_of_item in any_of:
          if "$ref" in any_of_item:
            #print("RECURSIVE_READ 3: %s" % (any_of_item))
            klass_str = any_of_item["$ref"].replace("#/definitions/", "")
            klass = Klass.get(klass_str)
            if instance[key] != None:
              instance[key] = klass.recursive_read(instance[key], store)
          elif "items" in any_of_item:
            if "$ref" in any_of_item["items"]:
              #print("RECURSIVE_READ 4: %s" % (any_of_item["items"]))
              #print("RECURSIVE_READ 5: %s" % (key))
              #print("RECURSIVE_READ 6: %s" % (instance[key]))
              klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
              klass = Klass.get(klass_str)
              result = []
              for item in instance[key]:
                result.append(klass.recursive_read(item, store))
              instance[key] = result
      elif "$ref" in definition:
        klass_str = definition["$ref"].replace("#/definitions/", "")
        klass = Klass.get(klass_str)
        if instance[key] != None:
          instance[key] = klass.recursive_read(instance[key], store)
    return instance