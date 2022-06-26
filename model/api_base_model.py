from pydantic import BaseModel
from uuid import uuid4
from store.store import Store
import json

class ApiBaseModel(BaseModel):

  def save(self, store, scope, use_scope=False):
    if use_scope:
      uuid = scope
    else:
      uuid = str(uuid4())
    uuid = store.put(self, self.__class__, uuid, scope)
    self.uuid = uuid
    return uuid

  def recursive_save(self, store, scope=None):

    from .klass import Klass

    use_scope = False
    if scope == None:
      scope = str(uuid4()) # Any unique string but use a UUID.
      use_scope = True
    schema = self.__class__.schema_json()
    x = json.loads(schema)
    for key, definition in x["properties"].items():
      if "anyOf" in definition:
        any_of = definition["anyOf"]
        for any_of_item in any_of:
          if "$ref" in any_of_item:
            klass_str = any_of_item["$ref"].replace("#/definitions/", "")
            klass = Klass.get(klass_str)
            if getattr(self, key) != None:
              setattr(self, key, klass.recursive_save(getattr(self, key), store, scope)) 
          elif "items" in any_of_item:
            if "$ref" in any_of_item["items"]:
              klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
              klass = Klass.get(klass_str)
              result = []
              for item in getattr(self, key):
                result.append(klass.recursive_save(item, store, scope))
              setattr(self, key, result)
      elif "$ref" in definition:
        klass_str = definition["$ref"].replace("#/definitions/", "")
        klass = Klass.get(klass_str)
        if getattr(self, key) != None:
          setattr(self, key, klass.recursive_save(getattr(self, key), store, scope)) 
    uuid = self.save(store, scope, use_scope)
    self.uuid = uuid
    return uuid

  @classmethod
  def read(cls, store, uuid):
    data = store.get(cls, uuid) 
    data["uuid"] = uuid
    return data

  @classmethod
  def recursive_read(cls, store, uuid):

    from .klass import Klass

    schema = cls.schema_json()
    instance = store.get(cls, uuid)
    x = json.loads(schema)
    for key, definition in x["properties"].items():
      if "anyOf" in definition:
        any_of = definition["anyOf"]
        for any_of_item in any_of:
          if "$ref" in any_of_item:
            klass_str = any_of_item["$ref"].replace("#/definitions/", "")
            klass = Klass.get(klass_str)
            if instance[key] != None:
              instance[key] = klass.recursive_read(store, instance[key])
          elif "items" in any_of_item:
            if "$ref" in any_of_item["items"]:
              klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
              klass = Klass.get(klass_str)
              result = []
              for item in instance[key]:
                result.append(klass.recursive_read(store, item))
              instance[key] = result
      elif "$ref" in definition:
        klass_str = definition["$ref"].replace("#/definitions/", "")
        klass = Klass.get(klass_str)
        if instance[key] != None:
          instance[key] = klass.recursive_read(store, instance[key])
    return instance

  @classmethod
  def list(cls, store):
    return store.list(cls)

  def check_and_save(self, store, item):
    if item == None:
      return None
    elif isinstance(item, str):
      return item
    else:
      return self.save(item)
  
  @classmethod
  def scope_reuse(cls):
    return True

  @classmethod
  def global_reuse(cls):
    return False

