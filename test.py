import sys
from factory.factory import *
from service.service import Service

procedure_code = code_data("767002", "SNOMED-CT", "2022-05-31", "White blood cell count")           
procedure_1 = procedure_data("Specimen Collection", procedure_code, None)
study_data_1 = study_data_data("Study Data 1", "Something", "Link 1")
activity_1 = activity_data("Activity_1", [procedure_1], [])
activity_2 = activity_data("Activity_2", [], [study_data_1])
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

phase = code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase IIa Trial")
study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
registry_type = code_data("C2365x", "http://www.cdisc.org", "1", "REGISTRY_STUDY_IDENTIFIER")
sponsor_type = code_data("C2365y", "http://www.cdisc.org", "1", "SPONSOR_STUDY_IDENTIFIER")
organisation_1 = organization_data("DUNS", "123456789", "ACME Pharma", sponsor_type)
organisation_2 = organization_data("FDA", "CT-GOV", "ClinicalTrials.gov", registry_type)
organisation_3 = organization_data("EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database", registry_type)
identifier_1 = study_identifier_data("CT-GOV-1234", organisation_2)
identifier_2 = study_identifier_data("EU-5678", organisation_3)
identifier_3 = study_identifier_data("ACME-5678", organisation_1)
identifiers = [identifier_1, identifier_2, identifier_3]

indication_1 = study_indication_data("Something bad", [code_data("C6666x", "http://www.cdisc.org", "1", "BAD STUFF")])
indication_2 = study_indication_data("Something similarly bad", [code_data("C6666y", "http://www.cdisc.org", "1", "BAD SIMILAR STUFF")])
origin_type = code_data("C6574y", "http://www.cdisc.org", "1", "SUBJECT DATA")
treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
study_arm_1 = study_arm_data("Placebo", "The Placebo Arm", placebo, "Captured subject data", origin_type)
study_arm_2 = study_arm_data("Active", "Super Drug Arm", treatment, "Captured subject data", origin_type)

#epoch_type = code_data("C1111x", "http://www.cdisc.org", "1", "NORMAL EPOCH")
run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
study_epoch_1 = study_epoch_data("Run In", "The run in", 1, run_in)
study_epoch_2 = study_epoch_data("Treatment", "The drug!", 2, treatment)
study_epoch_3 = study_epoch_data("Follow Up", "Go away", 3, follow_up)

start_rule = transition_rule_data("Start Rule")
end_rule = transition_rule_data("End Rule")
study_element_1 = study_element_data("Element 1", "First element", start_rule, end_rule)
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

#intent = code_data("C3495x", "http://www.cdisc.org", "1", "BIG INTENT")
#design_1_type = code_data("C3496x", "http://www.cdisc.org", "1", "COMPLEX DESIGN I")
#design_2_type = code_data("C3496y", "http://www.cdisc.org", "1", "COMPLEX DESIGN II")

intent = code_for('StudyDesign', 'trialIntentType', c_code='C15714')
print(intent)
design_1_type = code_for('StudyDesign', 'trialType', submission_value='BIOSIMILARITY')
print(design_1_type)
design_2_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
print(design_2_type)

design_1 = study_design_data([intent], design_1_type, study_cells, [indication_1], [objective_1], [population_1], [ii_1], [wf_1])
design_2 = study_design_data([intent], design_2_type, study_cells, [indication_1, indication_2], [objective_1], [population_1], [ii_1], [wf_1])
designs = [design_1, design_2]
final = code_data("C1113x", "http://www.cdisc.org", "1", "FINAL")
protocol_version_1 = study_protocol_version_data("Short", "Very Official", "Public Voice", "Incomprehensible", "1", None, "2022-01-01", final)
protocol_version_2 = study_protocol_version_data("Shorter", "Very Official", "Public Voice", "Incomprehensible", "1", "Amendment 1", "2022-02-01", final)
protocol_versions = [protocol_version_1, protocol_version_2]

study = study_data("New Title", "1", study_type, phase, identifiers, protocol_versions, designs)

print(study)

if __name__ == "__main__":
  service = Service(sys.argv)
  uuid = service.post("study_definitions", study)
  service.get("study_definitions", uuid)
  service.get("studies", uuid)
  items = ["studies", "study_identifiers", "organisations", "study_protocol_versions", "study_arms", "study_epochs", 
    "study_cells", "study_elements", "codes", "study_data", "procedures", "activities", "transition_rules"]
  for item in items:
    uuids = service.get(item)
    service.get(item, uuids[0])
