import yaml
import random
import string
from faker import Faker
from faker.providers import BaseProvider

code_index = 0
rule_index = 0
element_index = 0
fake = Faker()
Faker.seed(4321)

code_system_list = ["http://www.cdisc.org", "SNOMED-CT"]
organization_list = [
  ["DUNS", "123456789", "ACME Pharma"],
  ["FDA", "CT-GOV", "ClinicalTrials.gov"],
  ["EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database"]
]
study_identifier_list = ["CT-GOV-1234", "EU-5678", "ACME-5678"]

class DDFFakerProvider(BaseProvider):
    def activity(self, procedures, study_data, optional):
      i = fake.random.randint(1, 999)
      return {
        "activityId": "activity_%s" % i,
        "activityName": "Activity %s" % i,
        "activityDescription": fake.sentence(),
        "previousActivityId": None,
        "nextActivityId": None,
        "definedProcedures": procedures,
        "studyDataCollection": study_data,
        "activityIsOptional": optional,
        "activityIsOptionalReason": fake.sentence()
      }
    def address(self):
      return {
          "text": "123",
          "line": "fake",
          "city": "street",
          "district": "district 19",
          "state": "TX",
          "postalCode": "12345",
          "country": "USA"
      }
    def code(self):
      global code_index
      code_index += 1
      return {
        "codeId": "code_%s" % (code_index),
        "code": str(fake.random.randint(100000, 999999)),
        "codeSystem": code_system_list[fake.random.randint(0,len(code_system_list)-1)],
        "codeSystemVersion": "2022-03-25",
        "decode": fake.sentence()
      }
    def encounter(self, type, env_setting, contact_mode):
      i = fake.random.randint(1, 999)
      return {
        "encounterId": "encounter_%s" % i,
        "encounterName": "Encounter %s" % i,
        "encounterDescription": fake.sentence(),
        "previousEncounterId": None,
        "nextEncounterId": None,
        "encounterType": type,
        "encounterEnvironmentalSetting": env_setting,
        "encounterContactModes": [contact_mode],
        "transitionStartRule": None,
        "transitionEndRule": None
      }
    def endpoint(self):
      i = fake.random.randint(1, 999)
      return {
        "endpointId": "endpoint_%s" % i,
        "endpointDescription": "Endpoint %s" % i,
        "endpointPurposeDescription": fake.sentence(),
        "endpointLevel": fake.code()
      }
    def investigational_intervention(self):
      i = fake.random.randint(1, 999)
      return {
        "investigationalInterventionId": "intervention_%s" % i,
        "interventionDescription": "Intervention %s" % i,
        "codes": [fake.code(), fake.code()],
      }
    def objective(self):
      i = fake.random.randint(1, 999)
      return {
        "objectiveId": "objective_%s" % i,
        "objectiveDescription": "Objective Level %s" % i,
        "objectiveLevel": fake.code(),
        "objectiveEndpoints": [fake.endpoint(), fake.endpoint()]
      }
    def organization(self, code=None):
      if code == None:
        code = fake.code()
      org_identity = organization_list[fake.random.randint(0,len(organization_list)-1)]
      return {
        "organizationId": "organization_%s" % fake.random.randint(1, 999),
        "organisationIdentifierScheme": org_identity[0],
        "organisationIdentifier": org_identity[1],
        "organisationName": org_identity[2],
        "organisationType": code,
        "organizationLegalAddress": fake.address()
      }
    def procedure(self, code, optional):
      return {
        "procedureId": "procedure_%s" % fake.random.randint(1, 999),
        "procedureType": "Specimen Collection",
        "procedureCode": code,
        "procedureIsOptional": optional,
        "procedureIsOptionalReason": fake.sentence()
      }
    def study_arm(self, code):
      return {
        "studyArmId": "study_arm_%s" % fake.random.randint(1, 999),
        "studyArmName": "Active",
        "studyArmDescription": fake.sentence(),
        "studyArmType": code,
        "studyArmDataOriginDescription": "Captured subject data",
        "studyArmDataOriginType": fake.code(),
      }
    def study_cell(self, arm, epoch, elements):
      return {
        "studyCellId": "study_cell_%s" % fake.random.randint(1, 999),
        "studyArm": arm,
        "studyEpoch": epoch,
        "studyElements": elements
      }
    def study_data(self):
      i = fake.random.randint(1, 999)
      return {
        "studyDataId": "studydata_%s" % i,
        "studyDataName": "Study Data %s" % i,
        "studyDataDescription": fake.sentence(),
        "crfLink": "Link %s" % i,
      }
    def study_design(self, intent, types, model, therapeutic_areas, cells, indications, objectives, populations, interventions, workflows, estimands, encounters, activities):
      i = fake.random.randint(1, 999)
      return {
        "studyDesignId": "study_design_%s" % i,
        "studyDesignName": "Study Design%s" % i,
        "studyDesignDescription": fake.sentence(),
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
        "studyDesignRationale": fake.sentence()
      }
    def study_design_population(self):
      i = fake.random.randint(1, 999)
      return {
        'studyDesignPopulationId': "population_%s" % i,
        'populationDescription': "Population %s" % i,
        'plannedNumberOfParticipants': i,
        'plannedMaximumAgeOfParticipants': str(i),  
        'plannedMinimumAgeOfParticipants': str(i),
        'plannedSexOfParticipants': [fake.code()]
      }
    def study_element(self):
      global element_index
      element_index += 1
      return {
        "studyElementId": "element_%s" % (element_index),
        "studyElementName": "Element %s" % (element_index),
        "studyElementDescription": "%s Element" % (element_index),
        "transitionStartRule": fake.transition_rule(),
        "transitionEndRule": fake.transition_rule()
      }
    def study_epoch(self, epoch_type, encounters):
      i = fake.random.randint(1, 999)
      return {
        "studyEpochId": "study_epoch_%s" % i,
        "studyEpochName": "Study Epoch %s" % i,
        "studyEpochDescription": fake.sentence(),
        "previousStudyEpochId": None,
        "nextStudyEpochId": None,
        "studyEpochType": epoch_type,
        "encounters": encounters
      }
    def study_identifier(self, organisation):
      return {
        "studyIdentifierId": "study_identifier_%s" % fake.random.randint(1, 999),
        "studyIdentifier": study_identifier_list[fake.random.randint(0,len(study_identifier_list)-1)],
        "studyIdentifierScope": organisation
      }
    def study_indication(self):
      return {
        "indicationId": "study_indication_%s" % fake.random.randint(1, 999),
        "codes": [fake.code()],
        "indicationDescription": fake.sentence()
      }
    def transition_rule(self):
      global rule_index
      rule_index += 1
      return {
        "transitionRuleId": "rule_%s" % (rule_index),
        "transitionRuleDescription": "Rule: %s" % fake.sentence()
      }
    def workflow_item(self, encounter, activity):
      i = fake.random.randint(1, 999)
      return {
        'workflowItemId': "workflow_item_%s" % i,
        'workflowItemDescription': "Workflow item %s" % i,
        'previousWorkflowItemId': None,
        'nextWorkflowItemId': None,
        'workflowItemEncounterId': encounter,
        'workflowItemActivityId': activity,
      }
    def workflow(self, items):
      i = fake.random.randint(1, 999)
      return {
        'workflowId': "workflow_%s" % i,
        'workflowDesc': "Schedule of Activities",
        'workflowItems': items
      }

fake.add_provider(DDFFakerProvider)

def reset_code_index():
  global code_index
  code_index = 0
  global rule_index
  rule_index = 0
  global element_index
  element_index = 0

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
    
def code_data():
  return fake.code()

def code_for(klass, attribute, **kwargs):
  if 'c_code' in kwargs or 'submission_value' in kwargs:
    if 'c_code' in kwargs:
      entry = _find_ct_entry(klass, attribute, 'conceptId', kwargs['c_code'])
    elif 'submission_value' in kwargs:
      entry = _find_ct_entry(klass, attribute, 'submissionValue', kwargs['submission_value'])
    global code_index
    code_index += 1
    return {
      "codeId": "code_%s" % (code_index),
      "code": entry['conceptId'],
      "codeSystem": "http://www.cdisc.org",
      "codeSystemVersion": "2022-03-25",
      "decode": entry['preferredTerm']
    }
  else:
    raise Exception("Need to specify either a C Code or Submission value when selecting a CT value.")

def activity_data(procedures, study_data, optional=False):
  return fake.activity(procedures, study_data, optional)

def procedure_data(the_code, optional=False):
  return fake.procedure(the_code, optional)

def study_data_data():
  return fake.study_data()

def encounter_data(encounter_type, env_setting, contact_mode):
  return fake.encounter(encounter_type, env_setting, contact_mode)

def investigational_intervention_data():
  return fake.investigational_intervention()

def endpoint_data():
  return fake.endpoint()

def objective_data():
  return fake.objective()

def estimand_data(measure, population, treatment, variable, events):
  return { "summaryMeasure": measure, "analysisPopulation": population, "treatment": treatment, "variableOfInterest": variable, "intercurrentEvents": events }

def intercurrent_event_data(name, description, strategy):
  return { "intercurrentEventName": name, 
           "intercurrentEventDescription": description,
           "intercurrentEventStrategy": strategy
  }

def study_identifier_data(organisation):
  return fake.study_identifier(organisation)

def organization_data(organisation_type):
  return fake.organization(organisation_type)

def analysis_population_data(description):
  return {
    "populationDescription": description
  }

def study_design_population_data():
  return fake.study_design_population()
  
def study_arm_data(arm_type):
  return fake.study_arm(arm_type)

def study_epoch_data(epoch_type, encounters):
  return fake.study_epoch(epoch_type, encounters)

def study_cell_data(arm, epoch, elements):
  return fake.study_cell(arm, epoch, elements)

def study_element_data():
  return fake.study_element()

def transition_rule_data():
  return fake.transition_rule()

def study_indication_data():
  return fake.study_indication()

def study_data(title, version, type, phase, business_therapeutic_areas, identifiers, protocol_versions, designs):
  return {
    "studyId": None,
    "studyTitle": title,
    "studyVersion": version,
    "studyType":  type,
    "studyPhase":  phase,
    "businessTherapeuticAreas": business_therapeutic_areas,
    "studyIdentifiers": identifiers,
    "studyProtocolVersions": protocol_versions,
    "studyDesigns": designs,
    "studyRationale": fake.sentence(),
    "studyAcronym": "ABC"
  }

def study_design_data(intent, types, model, therapeutic_areas, cells, indications, objectives, populations, interventions, workflows, estimands, encounters, activities):
  return fake.study_design(intent, types, model, therapeutic_areas, cells, indications, objectives, populations, interventions, workflows, estimands, encounters, activities)

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

def workflow_item_data(encounter, activity):
  return fake.workflow_item(encounter, activity)

def workflow_data(items):
  return fake.workflow(items)

# Internal methods
def _find_ct_entry(klass, attribute, name, value):
  with open("data/ct.yaml") as file:
    ct = yaml.load(file, Loader=yaml.FullLoader)
    for entry in ct[klass][attribute]['terms']:
      if entry[name] == value:
        return entry
    raise Exception("Could not find CT match for (%s, %s, %s, %s)." % (klass, attribute, name, value))        

