from factory.factory import *
from model.study import Study
import inspect

class SimpleStudy():

  # def json():
  #   s = Study(studyId=None, studyTitle="foo", studyVersion="bar", studyRationale="baz", studyAcronym="poo")
 
  #   # getmembers() returns all the
  #   # members of an object
  #   for i in inspect.getmembmers(s):
        
  #       # to remove private and protected
  #       # functions
  #       if not i[0].startswith('_'):
            
  #           # To remove other methods that
  #           # doesnot start with a underscore
  #           if not inspect.ismethod(i[1]):
  #               print(i)

  def json():
    
    reset_code_index()
    
    procedure_code = code_data()           
    procedure_1 = procedure_data(procedure_code)
    study_data_1 = study_data_data()
    activity_1 = activity_data([procedure_1], [])
    activity_2 = activity_data([], [study_data_1])
    activities = [activity_1, activity_2]
    double_link(activities, 'activityId', 'previousActivityId', 'nextActivityId')

    encounter_type = code_data()
    env_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')    
    env_contact_mode = code_for('Encounter', 'encounterContactModes', c_code='C175574')    
    encounter_1 = encounter_data(encounter_type, env_setting, env_contact_mode)
    encounter_2 = encounter_data(encounter_type, env_setting, env_contact_mode)
    encounters = [encounter_1, encounter_2]
    double_link(encounters, 'encounterId', 'previousEncounterId', 'nextEncounterId')

    wfi_links = [
      [encounter_1, activity_1],
      [encounter_2, activity_2]
    ]
    wfis = []
    for item in wfi_links:
      wfis.append(workflow_item_data(item[0], item[1]))
    workflow = workflow_data(wfis)
    double_link(wfis, 'workflowItemId', 'previousWorkflowItemId', 'nextWorkflowItemId')  

    ii_1 = investigational_intervention_data()

    population_1 = study_design_population_data()

    objective_1 = objective_data()

    phase = code_data()
    study_type = code_data()
    registry_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Registry')
    sponsor_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Sponsor')
    regulator_type = code_for('Organization', 'organizationType', submission_value='Regulatory Agency')
    organisation_1 = organization_data(sponsor_type)
    organisation_2 = organization_data(registry_type)
    organisation_3 = organization_data(registry_type)
    identifier_1 = study_identifier_data(organisation_2)
    identifier_2 = study_identifier_data(organisation_3)
    identifier_3 = study_identifier_data(organisation_1)
    identifiers = [identifier_1, identifier_2, identifier_3]

    indication_1 = study_indication_data()
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    study_arm_1 = study_arm_data(placebo)
    study_arm_2 = study_arm_data(treatment)

    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    study_epoch_1 = study_epoch_data(run_in, [encounter_1, encounter_2])
    study_epoch_2 = study_epoch_data(treatment, [])
    study_epoch_3 = study_epoch_data(follow_up, [])
    epochs = [study_epoch_1, study_epoch_2, study_epoch_3]
    double_link(epochs, 'studyEpochId', 'previousStudyEpochId', 'nextStudyEpochId')
    #print(epochs)

    study_element_1 = study_element_data()
    study_element_2 = study_element_data()
    study_element_3 = study_element_data()
    study_element_4 = study_element_data()

    study_cells = []
    study_cells.append(study_cell_data(study_arm_1, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_2, [study_element_2]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_3, [study_element_4]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_2, [study_element_3]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_3, [study_element_4]))

    intent = code_for('StudyDesign', 'trialIntentType', c_code='C15714')
    trial_1_type = code_for('StudyDesign', 'trialType', submission_value='BIOSIMILARITY')
    trial_2_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='PARALLEL')

    therapeutic_areas = [code_data()]

    trial_types = [trial_1_type, trial_2_type]
    design_1 = study_design_data([intent], trial_types, int_model, therapeutic_areas, study_cells, [indication_1], [objective_1], [population_1], [ii_1], [workflow], [], [], [])
    designs = [design_1]
    protocol_version_1 = study_protocol_version_data("study_protocol_data_1", "Short", "Very Official", "Public Voice", "Incomprehensible", "1", None, "2022-01-01", code_data())
    protocol_version_2 = study_protocol_version_data("study_protocol_data_2", "Shorter", "Very Official", "Public Voice", "Incomprehensible", "1", "Amendment 1", "2022-02-01", code_data())
    protocol_versions = [protocol_version_1, protocol_version_2]

    business_therapeutic_areas = [code_data()]
    return study_data("Small Simple Test Study (SSTS)", "1", study_type, phase, business_therapeutic_areas, identifiers, protocol_versions, designs)
