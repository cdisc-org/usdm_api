from deta import Deta

class Store():
    
  def __init__(self):
    self.__deta = None
    self.__store = {}
    try: 
      self.__deta = Deta()
    except:
      self.__deta = None

  def put(self, klass, data, key):
    self.check(klass)
    if self.__deta == None:
      print("%s: %s -> %s" % (klass.upper(), key, data))
      self.__store[klass][key] = data
    else:
      print("%s: %s -> %s" % (klass.upper(), key, data))
      self.__store[klass].put(data, key)

  def get(self, klass, key):
    self.check(klass)
    if self.__deta == None:
      print("%s: %s" % (klass.upper(), key))
      return self.__store[klass][key]
    else:
      print("%s: %s" % (klass.upper(), key))
      return self.__store[klass].get(key)

  def list(self, klass):
    self.check(klass)
    items = None
    results = []
    print("List for: %s" % (klass))
    if self.__deta == None:
      items = self.__store[klass]
      print("Items: %s" % (items))
      for k, v in items.items():
        results.append(k)
    else:
      items = self.__store[klass].fetch().items
      print("Items: %s" % (items))
      for v in items:
        results.append(v["key"])
    print("Results: %s" % (results))
    return results

  def check(self, name):
    print("CHECK: >%s<" % (name))
    print("CHECK:", self.__store.keys())
    if not name in self.__store:
      print("CHECK: A")
      if self.__deta == None:
        self.__store[name] = {}
        print("CHECK: B")
      else:
        self.__store[name] = self.__deta.Base(name) 
        print("CHECK: C")
