import json
import requests

class Service():

  ENDPOINTS = { "remote": 'https://byrikz.deta.dev/', "local": 'http://localhost:8000/' }

  def __init__(self, argv):
    endpoint = "local"
    if len(argv) > 1 and argv[1].lower() == "remote":
      endpoint = "remote"
    self.url = self.ENDPOINTS[endpoint]

  def display_response(self, title, endpoint_url, r):
    resp = json.loads(r.text)
    print("%s (%s)" % (title, endpoint_url))
    print(json.dumps(resp, indent=4, sort_keys=True))
    print("")
    print("")

  def post(self, endpoint, body):
    endpoint_url = "%s%s" % (self.url, endpoint)
    r = requests.post(endpoint_url, data=json.dumps(body))
    self.display_response("Post", endpoint_url, r)
    return r.json()
  
  def get(self, endpoint, uuid=""):
    endpoint_url = "%s%s/%s" % (self.url, endpoint, uuid)
    r = requests.get(endpoint_url)
    self.display_response("Get", endpoint_url, r)
    return r.json()