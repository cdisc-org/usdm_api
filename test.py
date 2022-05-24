import sys
import json
import requests
from factory.factory import *

endpoints = { "remote": 'https://byrikz.deta.dev/', "local": 'http://localhost:8000/' }

activity_1 = activity_data("Activity_1")
activity_2 = activity_data("Activity_2")
procedure_1 = procedure_data("Procedure 1", None, None)
study_data_1 = study_data_data("Study Data 1", "Something", "Link 1")
encounter_1 = encounter_data("Encounter 1", "desc", None, None, None)
encounter_2 = encounter_data("Encounter 2", "desc", None, None, None)
wfi_1 = workflow_item_data("", None, None, None, encounter_1, activity_1)
wfi_2 = workflow_item_data("", None, None, None, encounter_2, activity_2)
wf_1 = workflow_data("Workflow 1", None, None, [wfi_1, wfi_2])

ii_1 = investigational_intervention_data(
  "Intervention 1", 
  "done", 
  [ 
    code_data("C7639x", "http://www.cdisc.org", "1", "MODEL 1"), 
    code_data("C7639y", "http://www.cdisc.org", "1", "MODEL 2")
  ]
)

population_1 = population_data("Population 1")

estimand_1 = estimand_data("Measure 1", population_1)

i_event_1 = intercurrent_event_data(
  "Intercurrent Event 1", 
  "An Event", 
  [ 
    code_data("C9822x", "http://www.cdisc.org", "1", "IE1"), 
    code_data("C9822y", "http://www.cdisc.org", "1", "IE2")
  ]
)
endpoint_1 = endpoint_data(
  "Endpoint 1", 
  code_data("C9834x", "http://www.cdisc.org", "1", "PURPOSE"), 
  code_data("C9834y", "http://www.cdisc.org", "1", "LEVEL")
  )
endpoint_2 = endpoint_data(
  "Endpoint 2", 
  code_data("C9834x", "http://www.cdisc.org", "1", "PURPOSE"), 
  code_data("C9834y", "http://www.cdisc.org", "1", "LEVEL")
  )
objective_1 = objective_data(
  "Objective Level 1", 
  code_data("C9844x", "http://www.cdisc.org", "1", "OBJ LEVEL"), 
  [endpoint_1, endpoint_2]
)

phase = code_data("C1234a", "http://www.cdisc.org", "1", "PHASE III")
study_type = code_data("C1254x", "http://www.cdisc.org", "1", "SIMPLE")
identifier_1 = study_identifier_data("A1", "X Registery", "Registry")
identifier_2 = study_identifier_data("A2", "X Registery", "Registry")
identifiers = [identifier_1, identifier_2]

indication_1 = study_indication_data("Something bad", [code_data("C6666x", "http://www.cdisc.org", "1", "BAD STUFF")])
indication_2 = study_indication_data("Something similarly bad", [code_data("C6666y", "http://www.cdisc.org", "1", "BAD SIMILAR STUFF")])
origin = code_data("C6574y", "http://www.cdisc.org", "1", "SUBJECT DATA")
origin_type = code_data("C6574z", "http://www.cdisc.org", "1", "SOMETHING")
arm_type = code_data("C6574x", "http://www.cdisc.org", "1", "NORMAL ARM")
epoch_type = code_data("C1111x", "http://www.cdisc.org", "1", "NORMAL EPOCH")
study_arm_1 = study_arm_data("Placebo", "The Placebo Arm", arm_type, origin, origin_type)
study_arm_2 = study_arm_data("Active", "Super Drug Arm", arm_type, origin, origin_type)
study_epoch_1 = study_epoch_data("Run In", "The run in", 1, epoch_type)
study_epoch_2 = study_epoch_data("Treatment", "The drug!", 1, epoch_type)
study_epoch_3 = study_epoch_data("Follow Up", "Go away", 1, epoch_type)
study_element_1 = study_element_data("Element 1", "First element")
study_element_2 = study_element_data("Element 2", "Second element")
study_element_3 = study_element_data("Element 3", "Third element")
study_element_4 = study_element_data("Element 4", "Fourth element")
study_element_5 = study_element_data("Element 5", "Fifth element")
study_element_6 = study_element_data("Element 6", "Sixth element")
study_cells = []
study_cells.append(study_cell_data(study_arm_1, study_epoch_1, [study_element_1]))
study_cells.append(study_cell_data(study_arm_1, study_epoch_2, [study_element_2]))
study_cells.append(study_cell_data(study_arm_1, study_epoch_3, [study_element_3]))
study_cells.append(study_cell_data(study_arm_2, study_epoch_1, [study_element_4]))
study_cells.append(study_cell_data(study_arm_2, study_epoch_2, [study_element_5]))
study_cells.append(study_cell_data(study_arm_2, study_epoch_3, [study_element_6]))
intent = code_data("C3495x", "http://www.cdisc.org", "1", "BIG INTENT")
design_1_type = code_data("C3496x", "http://www.cdisc.org", "1", "COMPLEX DESIGN I")
design_2_type = code_data("C3496y", "http://www.cdisc.org", "1", "COMPLEX DESIGN II")
design_1 = study_design_data(intent, design_1_type, study_cells, [indication_1], [objective_1], [population_1], [ii_1], [wf_1])
design_2 = study_design_data(intent, design_2_type, study_cells, [indication_1, indication_2], [objective_1], [population_1], [ii_1], [wf_1])
designs = [design_1, design_2]

study = study_data("New Title", "1", "draft", "", study_type, phase, identifiers, designs)

def print_response(title, r):
  resp = json.loads(r.text)
  print(title)
  print(json.dumps(resp, indent=4, sort_keys=True))
  print("")
  print("")

if __name__ == "__main__":
  endpoint = "local"
  if len(sys.argv) > 1 and sys.argv[1].lower() == "remote":
    endpoint = "remote"
  url = endpoints[endpoint]

  r = requests.post("%sstudy" % (url), data=json.dumps(study))
  print_response("Post Study", r)
  uuid = r.json()
  r = requests.get("%sstudy/%s" % (url, uuid))
  print_response("Get Study", r)
  r = requests.get("%sstudy_full/%s" % (url, uuid))
  print_response("Get Study Full", r)
  r = requests.get("%sstudy" % (url))
  print_response("List Studies", r)