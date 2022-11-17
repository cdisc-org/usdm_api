from factory.factory import *

class SimpleStudy():

  def json():

    reset_code_index()
    
    procedure_code = code_data("767002", "SNOMED-CT", "2022-05-31", "White blood cell count")           
    procedure_1 = procedure_data("proc_id", "Specimen Collection", procedure_code)
    study_data_1 = study_data_data("study_data_id", "Study Data 1", "Something", "Link 1")
    activity_1 = activity_data("activity_1", "A1", "Activity_1", [procedure_1], [])
    activity_2 = activity_data("activity_2", "A2", "Activity_2", [], [study_data_1])
    activities = [activity_1, activity_2]
    double_link(activities, 'activityId', 'previousActivityId', 'nextActivityId')

    encounter_type = code_data("C7652x", "http://www.cdisc.org", "1", "SITE VISIT")
    env_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')    
    env_contact_mode = code_for('Encounter', 'encounterContactMode', c_code='C175574')    
    encounter_1 = encounter_data("encounter_1", "Encounter 1", "desc", encounter_type, env_setting, env_contact_mode)
    encounter_2 = encounter_data("encounter_2", "Encounter 2", "desc", encounter_type, env_setting, env_contact_mode)
    encounters = [encounter_1, encounter_2]
    double_link(encounters, 'encounterId', 'previousEncounterId', 'nextEncounterId')

    wfi_links = [
      [encounter_1, activity_1],
      [encounter_2, activity_2]
    ]
    wfis = []
    for idx, item in enumerate(wfi_links):
      id = "workflow_item_%s" % (idx + 1)
      description = "Workflow item %s" % (idx + 1)
      wfis.append(workflow_item_data(id, description, item[0], item[1]))
    workflow = workflow_data("workflow_1", "Schedule of Activities", wfis)
    double_link(wfis, 'workflowItemId', 'previousWorkflowItemId', 'nextWorkflowItemId')  

    ii_1 = investigational_intervention_data(
      "Intervention 1", 
      [ 
        code_data("C7639x", "http://www.cdisc.org", "1", "MODEL 1"), 
        code_data("C7639y", "http://www.cdisc.org", "1", "MODEL 2")
      ]
    )

    population_1 = study_design_population_data("population_1", "Population 1")

    endpoint_1 = endpoint_data(
      "Endpoint 1", 
      "level description",
      code_data("C9834x", "http://www.cdisc.org", "1", "PURPOSE")
      )
    endpoint_2 = endpoint_data(
      "Endpoint 2",
      "level description",
      code_data("C9834x", "http://www.cdisc.org", "1", "PURPOSE"),
      )
    objective_1 = objective_data(
      "Objective Level 1", 
      code_data("C9844x", "http://www.cdisc.org", "1", "OBJ LEVEL"), 
      [endpoint_1, endpoint_2]
    )

    phase = code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase IIa Trial")
    study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
    registry_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Registry')
    sponsor_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Sponsor')
    regulator_type = code_for('Organization', 'organizationType', submission_value='Regulatory Agency')
    organisation_1 = organization_data("organization_1", "DUNS", "123456789", "ACME Pharma", sponsor_type)
    organisation_2 = organization_data("organization_2", "FDA", "CT-GOV", "ClinicalTrials.gov", registry_type)
    organisation_3 = organization_data("organization_3", "EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database", registry_type)
    identifier_1 = study_identifier_data("study_identifier_id_1", "CT-GOV-1234", organisation_2)
    identifier_2 = study_identifier_data("study_identifier_id_2", "EU-5678", organisation_3)
    identifier_3 = study_identifier_data("study_identifier_id_3", "ACME-5678", organisation_1)
    identifiers = [identifier_1, identifier_2, identifier_3]

    indication_1 = study_indication_data("study_idication_id_1", "Something bad", [code_data("C6666x", "http://www.cdisc.org", "1", "BAD STUFF")])
    indication_2 = study_indication_data("study_idication_id_2", "Something similarly bad", [code_data("C6666y", "http://www.cdisc.org", "1", "BAD SIMILAR STUFF")])
    origin_type = code_data("C6574y", "http://www.cdisc.org", "1", "SUBJECT DATA")
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    study_arm_1 = study_arm_data("study_arm_id_1", "Placebo", "The Placebo Arm", placebo, "Captured subject data", origin_type)
    study_arm_2 = study_arm_data("study_arm_id_2", "Active", "Super Drug Arm", treatment, "Captured subject data", origin_type)

    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    study_epoch_1 = study_epoch_data("study_epoch_data_id_1", "Run In", "The run in", run_in, [encounter_1, encounter_2])
    study_epoch_2 = study_epoch_data("study_epoch_data_id_2", "Treatment", "The drug!", treatment, [])
    study_epoch_3 = study_epoch_data("study_epoch_data_id_3", "Follow Up", "Go away", follow_up, [])
    epochs = [study_epoch_1, study_epoch_2, study_epoch_3]
    double_link(epochs, 'studyEpochId', 'previousStudyEpochId', 'nextStudyEpochId')
    #print(epochs)

    start_rule = transition_rule_data("start_1", "Start Rule")
    end_rule = transition_rule_data("end_1", "End Rule")
    study_element_1 = study_element_data("element_1", "Element 1", "First element", start_rule, end_rule)
    study_element_2 = study_element_data("element_2", "Element 2", "Second element")
    study_element_3 = study_element_data("element_3", "Element 3", "Third element")
    study_element_4 = study_element_data("element_4", "Element 4", "Fourth element")

    study_cells = []
    study_cells.append(study_cell_data("study_cell_1", study_arm_1, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data("study_cell_2", study_arm_1, study_epoch_2, [study_element_2]))
    study_cells.append(study_cell_data("study_cell_3", study_arm_1, study_epoch_3, [study_element_4]))
    study_cells.append(study_cell_data("study_cell_4", study_arm_2, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data("study_cell_5", study_arm_2, study_epoch_2, [study_element_3]))
    study_cells.append(study_cell_data("study_cell_6", study_arm_2, study_epoch_3, [study_element_4]))

    intent = code_for('StudyDesign', 'trialIntentType', c_code='C15714')
    trial_1_type = code_for('StudyDesign', 'trialType', submission_value='BIOSIMILARITY')
    trial_2_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    trial_types = [trial_1_type, trial_2_type]
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='PARALLEL')

    ta = code_data("123456789", "SNOMED", "2022", "Something")
    therapeutic_areas = [ta]

    design_1 = study_design_data("study_design_1", "Study Design", "foobar", [intent], trial_types, int_model, therapeutic_areas, study_cells, [indication_1], [objective_1], [population_1], [ii_1], [workflow], [], [], [])
    designs = [design_1]
    final = code_data("C1113x", "http://www.cdisc.org", "1", "FINAL")
    protocol_version_1 = study_protocol_version_data("study_protocol_data_1", "Short", "Very Official", "Public Voice", "Incomprehensible", "1", None, "2022-01-01", final)
    protocol_version_2 = study_protocol_version_data("study_protocol_data_2", "Shorter", "Very Official", "Public Voice", "Incomprehensible", "1", "Amendment 1", "2022-02-01", final)
    protocol_versions = [protocol_version_1, protocol_version_2]

    bta = code_data("12345", "Sponsor", "2022", "Business Unit A")
    business_therapeutic_areas = [bta]
    return study_data("Small Simple Test Study (SSTS)", "1", study_type, phase, business_therapeutic_areas, identifiers, protocol_versions, designs)
