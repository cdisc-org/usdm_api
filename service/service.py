import json
import requests

class Service():

  ENDPOINTS = { "remote": 'https://byrikz.deta.dev', "local": 'http://localhost:8000' }
  VERSION = "v1"
  
  def __init__(self, argv):
    endpoint = "local"
    if len(argv) > 1 and argv[1].lower() == "remote":
      endpoint = "remote"
    self.url = "%s/%s/" % (self.ENDPOINTS[endpoint], self.VERSION)

  def display_response(self, title, endpoint_url, r):
    resp = json.loads(r.text)
    print("%s (%s)" % (title, endpoint_url))
    print(json.dumps(resp, indent=4, sort_keys=True))
    print("")
    print("")

  def post(self, endpoint, body):
    print("Post ...")
    endpoint_url = "%s%s" % (self.url, endpoint)
    r = requests.post(endpoint_url, data=json.dumps(body))
    self.display_response("Post", endpoint_url, r)
    return r.json()
  
  def get(self, endpoint, uuid=""):
    print("Get ...")
    endpoint_url = "%s%s" % (self.url, endpoint)
    if uuid != "":
      endpoint_url = "%s/%s" % (endpoint_url, uuid)
    r = requests.get(endpoint_url)
    if r.status_code != 200:
      print("Get (%s)" % (endpoint_url))
      print("Bad response, code [%s], text [%s]" % (r.status_code, r.text))
      return {}
    else:
      self.display_response("Get", endpoint_url, r)
      return r.json()