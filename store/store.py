import os
import json
from deta import Deta

class Store():
    
  def __init__(self):
    self.__deta = Deta(os.environ['DDF_SERVICE_PROJ_KEY'])
    self.__store = self.__deta.Base("ddf_service")

  def put(self, data, klass, key):
    #self.__store.put(data, self.store_key(klass, key))
    self.__store.put(data.json(), self.store_key(klass, key))

  def get(self, klass, key):
    #data = self.__store.get(self.store_key(klass, key))
    data = json.loads(self.__store.get(self.store_key(klass, key))["value"])
    data.pop('key', None)
    return data

  def list(self, klass):
    results = []
    items = self.__store.fetch().items
    for v in items:
      if self.of_klass(klass, v["key"]):
        results.append(self.uuid_key(klass, v["key"]))
    return results

  def store_key(self, klass, key):
    return "%s.%s" % (klass, key)
  
  def uuid_key(self, klass, key):
    return key.replace("%s." % (klass), "")

  def of_klass(self, klass, key):
    return key.startswith("%s." % (klass))
