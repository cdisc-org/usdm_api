import os
import json
from deta import Deta

class Store():
    
  def __init__(self):
    self.__deta = Deta(os.environ['DDF_SERVICE_PROJ_KEY'])
    self.__store = self.__deta.Base("ddf_service")

  def put(self, data, klass, key, scope):
    value = data.json()
    match = self.matching(klass, data.json(), scope)
    if match == None:
      self.__store.put( { "value": value, "klass": klass.__name__,"scope": scope }, key)
      return key
    else:
      return match["key"]

  def get(self, klass, key):
    data = json.loads(self.__store.get(key)["value"])
    data.pop('key', None)
    data["uuid"] = key
    return data

  def scope(self, key):
    print(self.__store.get(key)["scope"])
    return self.__store.get(key)["scope"]

  def get_by_klass_and_scope(self, klass, scope):
    final_results = []
    results = self.__store.fetch([{"klass": klass}, {"scope": scope}])
    for item in results.items:
      data = json.loads(item["value"])
      key = item["key"]
      data.pop('key', None)
      data["uuid"] = key
      final_results.append(data)
    print(results)
    return final_results

  def get_by_klass(self, klass):
    final_results = []
    results = self.__store.fetch([{"klass": klass}])
    for item in results.items:
      data = json.loads(item["value"])
      key = item["key"]
      data.pop('key', None)
      data["uuid"] = key
      final_results.append(data)
    print(results)
    return final_results

  def list(self, klass):
    results = []
    items = self.__store.fetch({"klass": klass.__name__}).items
    for v in items:
      results.append(v["key"])
    return results

  def matching(self, klass, value, scope):
    #print("MATCHING:", klass.__name__)
    if klass.global_reuse():
      return self.global_match(klass, value)
    elif klass.scope_reuse():
      return self.scope_match(klass, value, scope)
    else:
      return None

  def global_match(self, klass, value):
    #print("GLOBAL:", klass.__name__)
    items = self.__store.fetch({"klass": klass.__name__, "value": value}).items
    for v in items:
      #print("GLOBAL: match")
      return v
    return None

  def scope_match(self, klass, value, scope):
    #print("SCOPE:", klass.__name__)
    items = self.__store.fetch({"klass": klass.__name__, "scope": scope, "value": value}).items
    for v in items:
      return v
    return None