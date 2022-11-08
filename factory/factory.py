import yaml
from uuid import uuid4

# def soa(df):
#   encounters = []
#   activities = []
#   # data = {'activity_1': ["x", "", "", ""], 'activity_2': ["", '', 'X', '']}
#   # pd.DataFrame.from_dict(data, orient='index', columns=['Visit 1', 'Visit 2', 'Visit 3', 'Visit 4'])
#   columns = df.columns.values.tolist()
#   rows = list(df.index)
#   for column in columns:
#     encounters.append(encounter_data(column, "The %s visit" % (column), None, None, None))
#   for row in rows:
#     activities.append(activity_data(row))
#   for index, row in df.iterrows():
#     for column in df:
#       if row[column].upper() == "X":
#         workflow_item_data("WFI %s,%s)", None, None, encounters[column], activities[row])

def double_link(items, prev, next):
  for item in items:
    item['uuid'] = str(uuid4())
  for idx, item in enumerate(items):
    if idx == 0:
      item[prev] = None
    else:
      item[prev] = items[idx-1]['uuid']
    if idx == len(items)-1:  
      item[next] = None
    else:
      item[next] = items[idx+1]['uuid']
    
def code_data(id, code, system, version, decode):
  return {
    "codeId": id,
    "code": code,
    "codeSystem": system,
    "codeSystemVersion": version,
    "decode": decode
  }

def code_for(klass, attribute, **kwargs):
  if 'c_code' in kwargs:
    entry = _find_ct_entry(klass, attribute, 'conceptId', kwargs['c_code'])
    # TODO: Where does the codeId come from here?
    return code_data("todo_1", entry['conceptId'], "http://www.cdisc.org", "2022-03-25", entry['preferredTerm'])
  elif 'submission_value' in kwargs:
    entry = _find_ct_entry(klass, attribute, 'submissionValue', kwargs['submission_value'])
    return code_data("todo_1", entry['conceptId'], "http://www.cdisc.org", "2022-03-25", entry['preferredTerm'])
  else:
    raise Exception("Need to specify either a C Code or Submission value when selecting a CT value.")

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

def activity_data(id, name, description, procedures, study_data):
  return {
    "activityId": id,
    "activityName": name,
    "activityDesc": description,
    "previousActivityId": None,
    "nextActivityId": None,
    "definedProcedures": procedures,
    "studyDataCollection": study_data
  }

def procedure_data(the_id, the_type, the_code):
  return {
    "procedureId": the_id,
    "procedureType": the_type,
    "procedureCode": the_code
  }

def study_data_data(id, name, description, link):
  return {
    "studyDataId": id,
    "studyDataName": name,
    "studyDataDesc": description,
    "crfLink": link
  }

def encounter_data(id, name, description, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None):
  return {
    "encounterId": id,
    "encounterName": name,
    "encounterDesc": description,
    "previousEncounterId": None,
    "nextEncounterId": None,
    "encounterType": encounter_type,
    "encounterEnvironmentalSetting": env_setting,
    "encounterContactMode": contact_mode,
    "transitionStartRule": start_rule,
    "transitionEndRule": end_rule
  }

def point_in_time_data(start, end, pit_type):
  return {
    "start_date": start,
    "end_date": end,
    "point_in_time_type": pit_type
  }

def investigational_intervention_data(description, codes):
  return {
    "codes": codes,
    "interventionDesc": description,
  }

def endpoint_data(description, purpose, level):
  return {
    "endpointDesc": description,
    "endpointPurposeDesc": purpose,
    "endpointLevel": level
  }

def objective_data(description, level, endpoints):
  return {
    "objectiveDesc": description,
    "objectiveLevel": level,
    "objectiveEndpoints": endpoints
  }

def estimand_data(measure, population, treatment, variable, events):
  return { "summaryMeasure": measure, "analysisPopulation": population, "treatment": treatment, "variableOfInterest": variable, "intercurrentEvents": events }

def intercurrent_event_data(name, description, strategy):
  return { "intercurrentEventName": name, 
           "intercurrentEventDesc": description,
           "intercurrentEventStrategy": strategy
  }

def study_identifier_data(id, identifier, organisation):
  return {
    "studyIdentifierId": id,
    "studyIdentifier": identifier,
    "studyIdentifierScope": organisation
  }

def organization_data(id, identifier_scheme, org_identifier, org_name, organisation_type):
  return {
    "organizationId": id,
    "organisationIdentifierScheme": identifier_scheme,
    "organisationIdentifier": org_identifier,
    "organisationName": org_name,
    "organisationType": organisation_type
  }

def analysis_population_data(description):
  return {
    "populationDesc": description
  }

def study_design_population_data(id, description):
  return {
    "studyDesignPopulationId": id,
    "populationDesc": description
  }
  
def study_arm_data(id, name, description, arm_type, origin_description, origin_type):
  return {
    "studyArmId": id,
    "studyArmName": name,
    "studyArmDesc": description,
    "studyArmType": arm_type,
    "studyArmDataOriginDesc": origin_description,
    "studyArmDataOriginType": origin_type,
  }

def study_epoch_data(id, name, description, epoch_type, encounters):
  return {
    "studyEpochId": id,
    "studyEpochName": name,
    "studyEpochDesc": description,
    "previousStudyEpochId": None,
    "nextStudyEpochId": None,
    "studyEpochType": epoch_type,
    "encounters": encounters
  }

def study_cell_data(id, arm, epoch, elements):
  return {
    "studyCellId": id,
    "studyArm": arm,
    "studyEpoch": epoch,
    "studyElements": elements
  }

def study_element_data(id, name, description, start=None, end=None):
  return {
    "studyElementId": id,
    "studyElementName": name,
    "studyElementDesc": description,
    "transitionStartRule": start,
    "transitionEndRule": end
  }

def transition_rule_data(id, description):
  return {
    "transitionRuleId": id,
    "transitionRuleDesc": description
  }

def study_indication_data(id, description, indications):
  return {
    "indicationId": id,
    "codes": indications,
    "indicationDesc": description
  }

def study_data(title, version, type, phase, business_therapeutic_areas, identifiers, protocol_versions, designs):
  return {
    "studyTitle": title,
    "studyVersion": version,
    "studyType":  type,
    "studyPhase":  phase,
    "businessTherapeuticAreas": business_therapeutic_areas,
    "studyIdentifiers": identifiers,
    "studyProtocolVersions": protocol_versions,
    "studyDesigns": designs
  }

def study_design_data(id, name, description, intent, types, model, therapeutic_areas, cells, indications, objectives, populations, interventions, workflows, estimands, encounters, activities):
  return {
    "studyDesignId": id,
    "studyDesignName": name,
    "studyDesignDescription": description,
    "trialIntentTypes": intent,
    "trialType": types,
    "interventionModel": model,
    "studyCells": cells,
    "studyIndications": indications,
    "studyInvestigationalInterventions": interventions,
    "studyStudyDesignPopulations": populations,
    "studyObjectives": objectives,
    "studyWorkflows": workflows,
    "therapeuticAreas:": therapeutic_areas,
    "studyEstimands": estimands,
    "encounters": encounters,
    "activities": activities,
  }

def study_protocol_version_data(id, brief_title, official_title, public_title, scientific_title, version, amendment, effective_date, status):
  return {
    "studyProtocolVersionId": id,
    "briefTitle": brief_title,
    "officialTitle": official_title,
    "publicTitle": public_title,
    "scientificTitle": scientific_title,
    "protocolVersion": version,
    "protocolAmendment": amendment,
    "protocolEffectiveDate": effective_date,
    "protocolStatus": status
  }

def workflow_item_data(description, encounter, activity):
  return {
    'workflowItemDesc': description,
    'workflowItemEncounter': encounter,
    'workflowItemActivity': activity,
  }

def workflow_data(id, description, items):
  return {
    'workflowId': id,
    'workflowDesc': description,
    'workflowItems': items
  }

# Internal methods
def _find_ct_entry(klass, attribute, name, value):
  with open("data/ct.yaml") as file:
    ct = yaml.load(file, Loader=yaml.FullLoader)
    for entry in ct[klass][attribute]['terms']:
      if entry[name] == value:
        return entry
    raise Exception("Could not find CT match for (%s, %s, %s, %s)." % (klass, attribute, name, value))        

