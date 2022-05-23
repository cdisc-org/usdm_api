import json
import requests

#url = 'https://byrikz.deta.dev/'
url = 'http://localhost:8000/'

def code_data(code, system, version, decode):
  return {
    "code": code,
    "code_system": system,
    "code_system_version": version,
    "decode": decode
  }

def study_data(title, version, status, protocol_version, type, phase, identifiers):
  return {
    "study_title": title,
    "study_version": version,
    "study_status": status,
    "study_protocol_version": protocol_version,
    "study_type":  type,
    "study_phase":  phase,
    "study_identifier": identifiers,
    "study_protocol_reference": None,
    "study_design": None
  }

def study_identifier_data(name, desc, org_code):
  return {
    "study_identifier_desc": name,
    "study_identifier_name": desc,
    "org_code": org_code
  }



def print_response(title, r):
  resp = json.loads(r.text)
  print(title)
  print(json.dumps(resp, indent=4, sort_keys=True))
  print("")
  print("")

phase = code_data("C1234", "http://www.cdisc.org", "1", "PHASE III")
type = code_data("C12546", "http://www.cdisc.org", "1", "SIMPLE")
identifiers = [study_identifier_data("A1", "X Registery", "Registry"), study_identifier_data("A2", "X Registery", "Registry")]
study = study_data("New Title", "1", "draft", "", type, phase, identifiers)
r = requests.post("%sstudy" % (url), data=json.dumps(study))
print_response("Post Study", r)
r = requests.get("%sstudy/%s" % (url, r.json()))
print_response("Get Study", r)
r = requests.get("%sstudy" % (url))
print_response("List Studies", r)

