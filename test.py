import json
import requests
from model.study import Study

#url = 'https://byrikz.deta.dev/'
url = 'http://localhost:8000/'

def code_data(code, system, version, decode):
  return {
    "code": code,
    "code_system": system,
    "code_system_version": version,
    "decode": decode
  }

def study_data(title, version, status, protocol_version, type, phase, identifiers, designs):
  return {
    "study_title": title,
    "study_version": version,
    "study_status": status,
    "study_protocol_version": protocol_version,
    "study_type":  type,
    "study_phase":  phase,
    "study_identifier": identifiers,
    "study_protocol_reference": None,
    "study_design": designs
  }

def study_identifier_data(name, desc, org_code):
  return {
    "study_identifier_desc": name,
    "study_identifier_name": desc,
    "org_code": org_code
  }

def study_design_data(intent, type, cells):
  return {
    "trial_intent_type": intent,
    "trial_type": type,
    "study_cell": cells
  }

def study_arm_data(name, description, arm_type, origin, origin_type):
  return {
    "study_arm_name": name,
    "study_arm_desc": description,
    "study_arm_origin": origin,
    "study_origin_type": origin_type,
    "study_arm_type": arm_type
  }

def study_epoch_data(name, description, sequence, epoch_type):
  return {
    "study_epoch_name": name,
    "study_epoch_desc": description,
    "sequence_in_study": sequence,
    "epoch_type": epoch_type
  }

def study_cell_data(arm, epoch):
  return {
    "study_arm": arm,
    "study_epoch": epoch
  }

def print_response(title, r):
  resp = json.loads(r.text)
  print(title)
  print(json.dumps(resp, indent=4, sort_keys=True))
  print("")
  print("")

phase = code_data("C1234a", "http://www.cdisc.org", "1", "PHASE III")
study_type = code_data("C1254x", "http://www.cdisc.org", "1", "SIMPLE")
identifier_1 = study_identifier_data("A1", "X Registery", "Registry")
identifier_2 = study_identifier_data("A2", "X Registery", "Registry")
identifiers = [identifier_1, identifier_2]

origin = code_data("C6574y", "http://www.cdisc.org", "1", "SUBJECT DATA")
origin_type = code_data("C6574z", "http://www.cdisc.org", "1", "SOMETHING")
arm_type = code_data("C6574x", "http://www.cdisc.org", "1", "NORMAL ARM")
epoch_type = code_data("C1111x", "http://www.cdisc.org", "1", "NORMAL EPOCH")
study_arm_1 = study_arm_data("Placebo", "The Placebo Arm", arm_type, origin, origin_type)
study_arm_2 = study_arm_data("Active", "Super Drug Arm", arm_type, origin, origin_type)
study_epoch_1 = study_epoch_data("Run In", "The run in", 1, epoch_type)
study_epoch_2 = study_epoch_data("Treatment", "The drug!", 1, epoch_type)
study_epoch_3 = study_epoch_data("Follow Up", "Go away", 1, epoch_type)
study_cells = []
study_cells.append(study_cell_data(study_arm_1, study_epoch_1))
study_cells.append(study_cell_data(study_arm_1, study_epoch_2))
study_cells.append(study_cell_data(study_arm_1, study_epoch_3))
study_cells.append(study_cell_data(study_arm_2, study_epoch_1))
study_cells.append(study_cell_data(study_arm_2, study_epoch_2))
study_cells.append(study_cell_data(study_arm_2, study_epoch_3))
intent = code_data("C3495x", "http://www.cdisc.org", "1", "BIG INTENT")
design_1_type = code_data("C3496x", "http://www.cdisc.org", "1", "COMPLEX DESIGN I")
design_2_type = code_data("C3496y", "http://www.cdisc.org", "1", "COMPLEX DESIGN II")
design_1 = study_design_data(intent, design_1_type, study_cells)
design_2 = study_design_data(intent, design_2_type, study_cells)
designs = [design_1, design_2]

study = study_data("New Title", "1", "draft", "", study_type, phase, identifiers, designs)

r = requests.post("%sstudy" % (url), data=json.dumps(study))
print_response("Post Study", r)
uuid = r.json()
r = requests.get("%sstudy/%s" % (url, uuid))
print_response("Get Study", r)
r = requests.get("%sstudy_full/%s" % (url, uuid))
print_response("Get Study Full", r)
r = requests.get("%sstudy" % (url))
print_response("List Studies", r)

#print(Study.schema_json(indent=2))

