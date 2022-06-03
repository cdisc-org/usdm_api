import os
import json
from deta import Deta

class Store():
    
  def __init__(self):
    self.__deta = Deta(os.environ['DDF_SERVICE_PROJ_KEY'])
    self.__store = self.__deta.Base("ddf_service")

  def put(self, data, klass, key):
    value = data.json()
    match = self.matching(klass, data.json())
    if match == None:
      self.__store.put( { "value": value, "klass": klass }, self.store_key(klass, key))
      return key
    else:
      return match["key"]


  def get(self, klass, key):
    data = json.loads(self.__store.get(self.store_key(klass, key))["value"])
    data.pop('key', None)
    data["uuid"] = key
    return data

  def list(self, klass):
    results = []
    items = self.__store.fetch({"klass": klass}).items
    for v in items:
      #if self.of_klass(klass, v["key"]):
      results.append(self.uuid_key(klass, v["key"]))
    return results

  def store_key(self, klass, key):
    #return "%s.%s" % (klass, key)
    return key
  
  def uuid_key(self, klass, key):
    #return key.replace("%s." % (klass), "")
    return key

  #def of_klass(self, klass, key):
  #  return key.startswith("%s." % (klass))

  def matching(self, klass, value):
    #if klass != "Code":
    #  return None
    #print("VALUE:", value)
    items = self.__store.fetch({"klass": klass, "value": value}).items
    #print("ITEMS:", items)
    for v in items:
      return v
    return None