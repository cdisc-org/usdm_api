import yaml
import random
import string
from faker import Faker
from faker.providers import BaseProvider

alias_code_index = 0
biomedical_concept_index = 0
bc_category_index = 0
bc_property_index = 0
bc_surrogate_index = 0
response_code_index = 0
code_index = 0
rule_index = 0
element_index = 0
fake = Faker()
Faker.seed(4321)

code_list = ["C15228", "C187674", "C156592", "C49659", "C28233"]
code_system_list = ["http://www.cdisc.org", "SNOMED-CT", "ISO 3166‑1 alpha3"]
organization_list = [
  ["DUNS", "123456789", "ACME Pharma"],
  ["FDA", "CT-GOV", "ClinicalTrials.gov"],
  ["EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database"]
]
study_identifier_list = ["CT-GOV-1234", "EU-5678", "ACME-5678"]

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

# Internal methods
def _find_ct_entry(klass, attribute, name, value):
  with open("data/ct.yaml") as file:
    ct = yaml.load(file, Loader=yaml.FullLoader)
    for entry in ct[klass][attribute]['terms']:
      if entry[name] == value:
        return entry
    raise Exception("Could not find CT match for (%s, %s, %s, %s)." % (klass, attribute, name, value))        

class DDFFakerProvider(BaseProvider):
    def activity(self, procedures, study_data, optional):
      i = fake.random.randint(1, 999)
      return {
        "activityId": "activity_%s" % i,
        "activityName": "Activity %s" % i,
        "activityDescription": fake.description("Activity %s" % i),
        "previousActivityId": None,
        "nextActivityId": None,
        "definedProcedures": procedures,
        "activityIsConditional": optional,
        "activityIsConditionalReason": fake.reason(),
        "biomedicalConcepts": ["ID_TBD"],
        "bcCategories": ["ID_TBD"],
        "bcSurrogates": ["ID_TBD"]
      }
    def address(self):
      return {
          "text": "123",
          "line": "fake street",
          "city": "some town",
          "district": "district 19",
          "state": "TX",
          "postalCode": "12345",
          "country": {
              "code": "USA",
              "codeSystem": "ISO 3166 1 alpha3",
              "codeSystemVersion": "",
              "decode": "United States of America"
          }
      }
    def alias_code(self):
      global alias_code_index
      alias_code_index += 1
      return {
        "aliasCodeId": "alias_code_%s" % (alias_code_index),
        "standardCode": code_for('StudyDesign', 'studyDesignBlindingSchema', submission_value='DOUBLE BLIND'),
        "standardCodeAliases": []
      }
    def biomedical_concept(self):
      global biomedical_concept_index
      biomedical_concept_index += 1
      return {
        "biomedicalConceptId": "biomedical_concept_%s" % (biomedical_concept_index),
        "bcName": "Biomedical Concept_%s" % (biomedical_concept_index),
        "bcSynonyms": ["bc_%s" % (biomedical_concept_index)],
        "bcReference": "BC ref_%s" % (biomedical_concept_index),
        "bcProperties": [fake.bc_property()],
        "bcConceptCode": fake.alias_code()
      }
    def bc_category(self):
      global bc_category_index
      bc_category_index += 1
      return {
        "biomedicalConceptCategoryId": "bc_category_%s" % (bc_category_index),
        "bcCategoryParents": ["ID_TBD"],
        "bcCategoryChildren": ["ID_TBD"],
        "bcCategoryName": "BC Category %s" % (bc_category_index),
        "bcCategoryDescription": fake.description("BC Category %s" % (bc_category_index)),
        "bcCategoryMemberIds": ["ID_TBD"]
      }
    def bc_property(self):
      global bc_property_index
      bc_property_index += 1
      return {
        "bcPropertyId": "bc_property_%s" % (bc_property_index),
        "bcPropertyName": "BC Property %s" % (bc_property_index),
        "bcPropertyRequired": False,
        "bcPropertyEnabled": False,
        "bcPropertyDatatype": "STRING",
        "bcPropertyResponseCodes": [fake.response_code()],
        "bcPropertyConceptCode": fake.alias_code()
      }
    def bc_surrogate(self):
      global bc_surrogate_index
      bc_surrogate_index += 1
      return {
        "bcSurrogateId": "bc_surrogate_%s" % (bc_property_index),
        "bcSurrogateName": "BC Surrogate %s" % (bc_property_index),
        "bcSurrogateDescription": fake.description("BC Surrogate %s" % (bc_property_index)),
        "bcSurrogateReference": ""
      }
    def code(self, code=None, system=None, version=None, decode=None):
      global code_index
      code_index += 1
      return {
        "codeId": "code_%s" % (code_index),
        "code": code if code is not None else code_list[fake.random.randint(0,len(code_list)-1)],
        "codeSystem": system if system is not None else code_system_list[fake.random.randint(0,len(code_system_list)-1)],
        "codeSystemVersion": version if version is not None else "2022-03-25",
        "decode": decode if decode is not None else "The preferred term for code_%s" % (code_index)
      }
    def description(self, name):
      return "A brief description for %s" % (name)
    def encounter(self, type, env_setting, contact_mode):
      i = fake.random.randint(1, 999)
      return {
        "encounterId": "encounter_%s" % i,
        "encounterName": "Encounter %s" % i,
        "encounterDescription": fake.description("Encounter %s" % i),
        "previousEncounterId": None,
        "nextEncounterId": None,
        "encounterType": type,
        "encounterEnvironmentalSetting": env_setting,
        "encounterContactModes": [contact_mode],
        "transitionStartRule": None,
        "transitionEndRule": None
      }
    def endpoint(self, code=None):
      i = fake.random.randint(1, 999)
      return {
        "endpointId": "endpoint_%s" % i,
        "endpointDescription": "Endpoint %s" % i,
        "endpointPurposeDescription": fake.description("Endpoint %s" % i),
        "endpointLevel": code if code is not None else fake.code()
      }
    def investigational_intervention(self):
      i = fake.random.randint(1, 999)
      return {
        "investigationalInterventionId": "intervention_%s" % i,
        "interventionDescription": "Intervention %s" % i,
        "codes": [fake.code(code="XX031ZA", system="ATC", version="2021", decode="SubstX"), 
                  fake.code(code="L01XK01", system="ATC", version="14-12-2021", decode="Olaparib")],
      }
    def objective(self):
      i = fake.random.randint(1, 999)
      return {
        "objectiveId": "objective_%s" % i,
        "objectiveDescription": "Objective Level %s" % i,
        "objectiveLevel": code_for('Objective', 'objectiveLevel', submission_value='Study Primary Objective'),
        "objectiveEndpoints": [fake.endpoint(code_for('Endpoint', 'endpointLevel', submission_value='Primary Endpoint')), 
                               fake.endpoint(code_for('Endpoint', 'endpointLevel', submission_value='Secondary Endpoint'))]
      }
    def organization(self, code=None):
      org_identity = organization_list[fake.random.randint(0,len(organization_list)-1)]
      return {
        "organizationId": "organization_%s" % fake.random.randint(1, 999),
        "organisationIdentifierScheme": org_identity[0],
        "organisationIdentifier": org_identity[1],
        "organisationName": org_identity[2],
        "organisationType": code if code else fake.code(),
        "organizationLegalAddress": fake.address()
      }
    def procedure(self, code=None, optional=None):
      return {
        "procedureId": "procedure_%s" % fake.random.randint(1, 999),
        "procedureType": "Specimen Collection",
        "procedureCode": code if code else fake.code(),
        "procedureIsConditional": optional if optional else False,
        "procedureIsConditionalReason": fake.reason()
      }
    def reason(self):
      return "Because of a stipulation or requirement"
    def response_code(self):
      global response_code_index
      response_code_index += 1
      return {
        "responseCodeId": "response_code_%s" % (response_code_index),
        "responseCodeEnabled": False,
        "code": fake.code()
      }
    def study_arm(self, code=None):
      studyArmId = "study_arm_%s" % fake.random.randint(1, 999)
      return {
        "studyArmId": studyArmId,
        "studyArmName": "Active",
        "studyArmDescription": fake.description(studyArmId),
        "studyArmType": code if code else fake.code(),
        "studyArmDataOriginDescription": "Captured subject data",
        "studyArmDataOriginType": code_for('StudyArm', 'studyArmDataOriginType', submission_value='Data Generated Within Study'),
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
        "studyDataDescription": fake.description("Study Data %s" % i),
        "crfLink": "Link %s" % i,
      }
    def study_design(self, intent, types, model, therapeutic_areas, cells, indications, objectives, populations, interventions, workflows, estimands, encounters, activities):
      i = fake.random.randint(1, 999)
      return {
        "studyDesignId": "study_design_%s" % i,
        "studyDesignName": "Study Design%s" % i,
        "studyDesignDescription": fake.description("Study Design%s" % i),
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
        "studyDesignRationale": fake.reason(),
        "studyDesignBlindingScheme": fake.alias_code(),
        "biomedicalConceptIds": fake.biomedical_concept(),
        "bcCategoryIds": fake.bc_category(),
        "bcSurrogateIds": fake.bc_surrogate()
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
        "studyEpochDescription": fake.description("Study Epoch %s" % i),
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
      indicationId = "study_indication_%s" % fake.random.randint(1, 999)
      return {
        "indicationId": indicationId,
        "codes": [fake.code()],
        "indicationDescription": fake.description(indicationId)
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
        'workflowItemEncounterId': "ID_TBD",
        'workflowItemActivityId': "ID_TBD",
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
