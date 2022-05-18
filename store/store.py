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
      #print("%s -> %s" % (key, data))
      self.__store[klass][key] = data
    else:
      self.__store[klass].put(data, key)

  def get(self, klass, key):
    self.check(klass)
    if self.__deta == None:
      #print("%s" % (key))
      return self.__store[klass][key]
    else:
      return self.__store[klass].get(key)

  def list(self, klass):
    self.check(klass)
    items = None
    results = []
    if self.__deta == None:
      #print("%s" % (key))
      items = self.__store[klass]
    else:
      items = self.__store[klass].fetch()
    for k, v in items.items():
      results.append(k)
    return results

  def check(self, name):
    if not name in self.__store:
      if self.__deta == None:
        self.__store[name] = {}
      else:
        self.__store[name] = self.__deta.Base(name) 