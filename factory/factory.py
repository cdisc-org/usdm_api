import yaml
from model.activity import Activity

code_index = 0

def reset_code_index():
  global code_index
  code_index = 0

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

def double_link(items, id, prev, next):
  for idx, item in enumerate(items):
    if idx == 0:
      item[prev] = None
    else:
      item[prev] = items[idx-1][id]
    if idx == len(items)-1:  
      item[next] = None
    else:
      item[next] = items[idx+1][id]
    
def code_data(code, system, version, decode):
  global code_index
  code_index += 1
  return {
    "codeId": "code_%s" % (code_index),
    "code": code,
    "codeSystem": system,
    "codeSystemVersion": version,
    "decode": decode
  }

def code_for(klass, attribute, **kwargs):
  if 'c_code' in kwargs:
    entry = _find_ct_entry(klass, attribute, 'conceptId', kwargs['c_code'])
    return code_data(entry['conceptId'], "http://www.cdisc.org", "2022-03-25", entry['preferredTerm'])
  elif 'submission_value' in kwargs:
    entry = _find_ct_entry(klass, attribute, 'submissionValue', kwargs['submission_value'])
    return code_data(entry['conceptId'], "http://www.cdisc.org", "2022-03-25", entry['preferredTerm'])
  else:
    raise Exception("Need to specify either a C Code or Submission value when selecting a CT value.")

def activity_data(id, name, description, procedures, **kwargs):
  return {
    "activityId": id,
    "activityName": name,
    "activityDescription": description,
    "previousActivityId": kwargs['previous_activity_id'] if 'previous_activity_id' in kwargs else None,
    "nextActivityId": kwargs['next_activity_id'] if 'next_activity_id' in kwargs else None,
    "definedProcedures": procedures,
    "activityIsConditional": kwargs['conditional'] if 'conditional' in kwargs else False,
    "activityIsConditionalReason": kwargs['conditional_reason'] if 'conditional_reason' in kwargs else "",
    "biomedicalConcepts": kwargs['biomedical_concepts'] if 'biomedical_concepts' in kwargs else [],
    "bcCategories": kwargs['bc_categories'] if 'bc_categories' in kwargs else [],
    "bcSurrogates": kwargs['bc_surrogates'] if 'bc_surrogates' in kwargs else [],
  }

def procedure_data(the_id, the_type, the_code, **kwargs):
  return {
    "procedureId": the_id,
    "procedureType": the_type,
    "procedureCode": the_code,
    "procedureIsConditional": kwargs['conditional'] if 'conditional' in kwargs else False,
    "procedureIsConditionalReason": kwargs['conditional_reason'] if 'conditional_reason' in kwargs else "",
  }

def encounter_data(id, name, description, encounter_type, env_setting, contact_mode, **kwargs):
  return {
    "encounterId": id,
    "encounterName": name,
    "encounterDescription": description,
    "previousEncounterId": kwargs['previous_activity_id'] if 'previous_activity_id' in kwargs else None,
    "nextEncounterId": kwargs['next_activity_id'] if 'next_activity_id' in kwargs else None,
    "encounterType": encounter_type,
    "encounterEnvironmentalSetting": env_setting,
    "encounterContactMode": contact_mode,
    "transitionStartRule": kwargs['start_rule'] if 'start_rule' in kwargs else None,
    "transitionEndRule": kwargs['end_rule'] if 'end_rule' in kwargs else None,
  }

def investigational_intervention_data(id, description, codes):
  return {
    "investigationalInterventionId": id,
    "interventionDescription": description,
    "codes": codes,
  }

def endpoint_data(id, description, purpose, level):
  return {
    "endpointId": id,
    "endpointDescription": description,
    "endpointPurposeDescription": purpose,
    "endpointLevel": level,
  }

def objective_data(id, description, level, endpoints):
  return {
    "objectiveId": id,
    "objectiveDescription": description,
    "objectiveLevel": level,
    "objectiveEndpoints": endpoints,
  }

def estimand_data(id, measure, population, treatment, variable, events):
  return {
    "estimandId": id, 
    "summaryMeasure": measure, 
    "analysisPopulation": population, 
    "treatment": treatment, 
    "variableOfInterest": variable, 
    "intercurrentEvents": events,
  }

def intercurrent_event_data(id, name, description, strategy):
  return { 
    "intercurrentEventId": id,
    "intercurrentEventName": name, 
    "intercurrentEventDescription": description,
    "intercurrentEventStrategy": strategy,
  }

def study_identifier_data(id, identifier, organisation):
  return {
    "studyIdentifierId": id,
    "studyIdentifier": identifier,
    "studyIdentifierScope": organisation,
  }

def organization_data(id, identifier_scheme, org_identifier, org_name, organisation_type, **kwargs):
  return {
    "organizationId": id,
    "organisationIdentifierScheme": identifier_scheme,
    "organisationIdentifier": org_identifier,
    "organisationName": org_name,
    "organisationType": organisation_type,
    "organizationLegalAddress": kwargs['address'] if 'address' in kwargs else None,
  }

def analysis_population_data(id, description):
  return {
    "analysisPopulationId": id,
    "populationDescription": description,
  }

def study_design_population_data(id, description, **kwargs):
  return {
    "studyDesignPopulationId": id,
    "populationDescription": description,
    "plannedNumberOfParticipants": kwargs['num'] if 'num' in kwargs else 0,
    "plannedMaximumAgeOfParticipants": kwargs['max_age'] if 'max_age' in kwargs else "",  
    "plannedMinimumAgeOfParticipants": kwargs['min_age'] if 'min_age' in kwargs else "",
    "plannedSexOfParticipants": kwargs['sex'] if 'sex' in kwargs else [],
  }
  
def study_arm_data(id, name, description, arm_type, origin_description, origin_type):
  return {
    "studyArmId": id,
    "studyArmName": name,
    "studyArmDescription": description,
    "studyArmType": arm_type,
    "studyArmDataOriginDescription": origin_description,
    "studyArmDataOriginType": origin_type,
  }

def study_epoch_data(id, name, description, epoch_type, encounters):
  return {
    "studyEpochId": id,
    "studyEpochName": name,
    "studyEpochDescription": description,
    "studyEpochType": epoch_type,
    "previousStudyEpochId": None,
    "nextStudyEpochId": None,
    "encounters": encounters,
  }

def study_cell_data(id, arm, epoch, elements):
  return {
    "studyCellId": id,
    "studyArm": arm,
    "studyEpoch": epoch,
    "studyElements": elements,
  }

def study_element_data(id, name, description, **kwargs):
  return {
    "studyElementId": id,
    "studyElementName": name,
    "studyElementDescription": description,
    "transitionStartRule": kwargs['start'] if 'start' in kwargs else None,
    "transitionEndRule": kwargs['end'] if 'end' in kwargs else None,
  }

def transition_rule_data(id, description):
  return {
    "transitionRuleId": id,
    "transitionRuleDescription": description,
  }

def study_indication_data(id, description, indications):
  return {
    "indicationId": id,
    "indicationDescription": description,
    "codes": indications,
  }

def study_data(title, version, type, phase, business_therapeutic_areas, identifiers, protocol_versions, designs, **kwargs):
  return {
    "studyId": kwargs['id'] if 'id' in kwargs else None,
    "studyTitle": title,
    "studyVersion": version,
    "studyType":  type,
    "studyPhase":  phase,
    "businessTherapeuticAreas": business_therapeutic_areas,
    "studyIdentifiers": identifiers,
    "studyProtocolVersions": protocol_versions,
    "studyDesigns": designs,
    "studyRationale": kwargs['rationale'] if 'rationale' in kwargs else "",
    "studyAcronym": kwargs['acronym'] if 'acronym' in kwargs else "",
  }

def study_design_data(id, name, description, intent, types, model, therapeutic_areas, cells, indications, objectives, populations, interventions, workflows, estimands, encounters, activities, rationale, **kwargs):
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
    "studyScheduleTimelines": workflows,
    "therapeuticAreas:": therapeutic_areas,
    "studyEstimands": estimands,
    "encounters": encounters,
    "activities": activities,
    "studyDesignRationale": rationale,
    "studyDesignBlindingScheme": kwargs['scheme'] if 'scheme' in kwargs else None,
    "biomedicalConcepts": kwargs['biomedical_concepts'] if 'biomedical_concepts' in kwargs else [],
    "bcCategories": kwargs['bc_categories'] if 'bc_categories' in kwargs else [],
    "bcSurrogates": kwargs['bc_surrogates'] if 'bc_surrogates' in kwargs else [],
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
    "protocolStatus": status,
  }

def workflow_item_data(id, description, **kwargs):
  return {
    'workflowItemId': id,
    'workflowItemDescription': description,
    'previousWorkflowItemId': kwargs['previous_workflow_id'] if 'previous_workflow_id' in kwargs else None,
    'nextWorkflowItemId': kwargs['next_workflow_id'] if 'next_workflow_id' in kwargs else None,
    'workflowItemEncounterId': kwargs['encounter'] if 'encounter' in kwargs else None,
    'workflowItemActivityId': kwargs['activity'] if 'activity' in kwargs else None,
  }

def workflow_data(id, description, items):
  return {
    'workflowId': id,
    'workflowDescription': description,
    'workflowItems': items,
  }

def address_data(id, text, line, city, district, state, postal_code, country):
  return{
    "addressId": id,
    "text": text,
    "line": line,
    "city": city,
    "district": district,
    "state": state,
    "postalCode": postal_code,
    "country": country,
  }

def alias_code_data(id, code, **kwargs):
  return{
    "aliasCodeId": id,
    "standardCode": code,
    "standardCodeAliases": kwargs['code_alias'] if 'code_alias' in kwargs else [],
  }

def biomedical_concept_data(id, name, reference, concept_code, **kwargs):
  return {
    "biomedicalConceptId": id,
    "bcName": name,
    "bcSynonyms": kwargs['synonyms'] if 'synonyms' in kwargs else [],
    "bcReference": reference,
    "bcProperties": kwargs['properties'] if 'properties' in kwargs else [],
    "bcConceptCode": concept_code,
  }

def bc_category_data(id, name, description, **kwargs):
  return {
    "biomedicalConceptCategoryId": id, 
    "bcCategoryChildIds": kwargs['children_ids'] if 'children_ids' in kwargs else [],
    "bcCategoryName": name,
    "bcCategoryDescription": description,
    "bcCategoryMemberIds": kwargs['member_ids'] if 'member_ids' in kwargs else [],
    "bcCategoryCode": kwargs['bcCategoryCode'] if 'bcCategoryCode' in kwargs else [],
  }

def bc_property_data(id, name, required, enabled, datatype, concept_code, **kwargs):
  return {
    "bcPropertyId": id,
    "bcPropertyName": name,
    "bcPropertyRequired": required,
    "bcPropertyEnabled": enabled,
    "bcPropertyDatatype": datatype,
    "bcPropertyResponseCodes": kwargs['response_codes'] if 'response_codes' in kwargs else [],
    "bcPropertyConceptCode": concept_code,
  }

def bc_surrogate_data(id, name, description, reference):
  return {
    "bcSurrogateId": id,
    "bcSurrogateName": name,
    "bcSurrogateDescription": description,
    "bcSurrogateReference": reference,
  }

# Internal methods
def _find_ct_entry(klass, attribute, name, value):
  with open("data/ct.yaml") as file:
    ct = yaml.load(file, Loader=yaml.FullLoader)
    for entry in ct[klass][attribute]['terms']:
      if entry[name] == value:
        return entry
    raise Exception("Could not find CT match for (%s, %s, %s, %s)." % (klass, attribute, name, value))        
