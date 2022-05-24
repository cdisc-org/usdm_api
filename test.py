import json
import requests

url = 'https://byrikz.deta.dev/'
#url = 'http://localhost:8000/'

def code_data(code, system, version, decode):
  return {
    "code": code,
    "code_system": system,
    "code_system_version": version,
    "decode": decode
  }

def workflow_data(description, start, end, items):
  return {
    "workflow_desc": description,
    "workflow_start_point": start,
    "workflow_end_point": end,
    "workflow_item": items
  }

def workflow_item_data(description, from_pit, to_pit, previous, encounter, activity):
  return {
    "description": description,
    "from_point_in_time": from_pit,
    "to_point_in_time": to_pit,
    "previous_workflow_item": previous,
    "encounter": encounter,
    "activity": activity
  }

def activity_data(description):
  return {
    "activity_desc": description
  }

def procedure_data(name, the_type, previous):
  return {
    "procedure_name": name,
    "procedure_type": the_type,
    "previous_procedure": previous
  }

def study_data_data(name, description, link):
  return {
    "study_data_name": name,
    "study_data_desc": description,
    "crf_link": link
  }

def encounter_data(name, description, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None):
  return {
    "encounter_desc": description,
    "name": name,
    "encounter_type": encounter_type,
    "env_setting": env_setting,
    "contact_mode": contact_mode,
    "start_rule": start_rule,
    "end_rule": end_rule
  }

def point_in_time_data(start, end, pit_type):
  return {
    "start_date": start,
    "end_date": end,
    "point_in_time_type": pit_type
  }

def investigational_intervention_data(description, status, models):
  return {
    "intervention_desc": description,
    "intervention_status": status,
    "intervention_model": models
  }

def endpoint_data(description, purpose, level):
  return {
    "endpoint_desc": description,
    "endpoint_purpose": purpose,
    "outcome_level": level
  }

def objective_data(description, level, endpoints):
  return {
    "objective_desc": description,
    "objective_endpoint": endpoints,
    "objective_level": level
  }

def population_data(description):
  return { "population_desc": description }

def estimand_data(measure, population):
  return { "summary_measure": measure, "population": population }

def intercurrent_event_data(name, description, coding):
  return { "intercurrent_name": name, 
           "intercurrent_desc": description,
           "coding": coding
  }

def study_identifier_data(name, desc, org_code):
  return {
    "study_identifier_desc": name,
    "study_identifier_name": desc,
    "org_code": org_code
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

def study_cell_data(arm, epoch, elements):
  return {
    "study_arm": arm,
    "study_epoch": epoch,
    "study_element": elements
  }

def study_element_data(name, description, start = None, end = None):
  return {
    "study_element_name": name,
    "study_element_desc": description,
    "start_rule": start,
    "end_rule": end
  }

def rule_data(description):
  return {
    "rule_desc": description
  }

def study_indication_data(description, indications):
  return {
    "indication_desc": description,
    "indication": indications
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

def study_design_data(intent, type, cells, indications, objectives, populations, interventions, workflows):
  return {
    "trial_intent_type": intent,
    "trial_type": type,
    "study_cell": cells,
    "study_indication": indications,
    "study_objective": objectives,
    "study_population": populations,
    "study_investigational_interventions": interventions,
    "study_workflow": workflows
  }

def print_response(title, r):
  resp = json.loads(r.text)
  print(title)
  print(json.dumps(resp, indent=4, sort_keys=True))
  print("")
  print("")

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

r = requests.post("%sstudy" % (url), data=json.dumps(study))
print_response("Post Study", r)
uuid = r.json()
#r = requests.get("%sstudy/%s" % (url, uuid))
#print_response("Get Study", r)
r = requests.get("%sstudy_full/%s" % (url, uuid))
print_response("Get Study Full", r)
#r = requests.get("%sstudy" % (url))
#print_response("List Studies", r)