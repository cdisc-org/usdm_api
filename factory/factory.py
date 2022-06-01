def soa(df):
  encounters = []
  activities = []
  # data = {'activity_1': ["x", "", "", ""], 'activity_2': ["", '', 'X', '']}
  # pd.DataFrame.from_dict(data, orient='index', columns=['Visit 1', 'Visit 2', 'Visit 3', 'Visit 4'])
  columns = df.columns.values.tolist()
  rows = list(df.index)
  for column in columns:
    encounters.append(encounter_data(column, "The %s visit" % (column), None, None, None))
  for row in rows:
    activities.append(activity_data(row))
  for index, row in df.iterrows():
    for column in df:
      if row[column].upper() == "X":
        workflow_item_data("WFI %s,%s)", None, None, encounters[column], activities[row])

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

def study_identifier_data(identifier, identifier_type, org_name):
  return {
    "study_identifier": identifier,
    "study_identifier_type": identifier_type,
    "organization_name": org_name
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
