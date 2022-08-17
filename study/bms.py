from factory.factory import *

class BMS():

  def json():

    # Rules
    study_rule_data = [
      "DO NOT USE - INDEX 0",

      # Visit Start Rules
      "6 weeks prior to treatment",
      "2 hours before treatment",
      "start of day 15",
      "start of day 22",
      "start of day 36",
      "Start of day 43",
      "Start of day 64",
      "Start of day 85",
      "Start of day 106",
      "Start of day 127",
      "Start of day 148",
      "Start of day 169",
      "",

      # Visit End Rules
      "start of run-in period",
      "",
      "end of day 15",
      "end of day 22",
      "End of day 36",
      "End of day 43",
      "End of day 64",
      "End of day 85",
      "End of day 106",
      "End of day 127",
      "End of day 148",
      "End of day 169",
      ""

      # Element Start Rules
      "6 weeks prior to treatment",
      "Start of treatment period",
      "Start of treatment period",
      "Start of treatment period",
      "Start of treatment period",
      "",
      "",
		
      # Element End Rules
      "Start of run-in period",
      "end of treatment period",
      "end of treatment period",
      "end of treatment period",
      "end of treatment period",
      "",
      ""

    ]

    rules = []
    for rule in study_rule_data:
      rules.append(transition_rule_data(rule))

    # Code references
    code_1 = code_data( "24662006", "SNOMED-CT", "4.0.6.4", "Influenza due to Influenza virus, type B")
    code_2 = code_data( "1022000", "MEDDRA", "Nov18_2021", "Influenza")
    code_3 = code_data( "J11.1", "ICD	10", "1", "Influenza due to unidentified influenza virus with other respiratory manifestations")
    code_4 = code_data( "C22.1", "ICD	10", "1", "Intrahepatic bile duct carcinoma")
    code_5 = code_data( "371970002", "SNOMED-CT", "4.0.6.4", "Primary malignant neoplasm of biliary tract (disorder)")
    code_6 = code_data( "10004596", "MEDDRA", "Nov18_2021", "Bile duct cancer recurrent")
    code_7 = code_data( "J07BX03", "ATC	2020", "1", "Covid-19 vaccines")
    code_8 = code_data( "L01XC28", "ATC", "14-12-2021", "Durvalumab")
    code_9 = code_data( "L01XK01", "ATC", "14-12-2021", "Olaparib")
    code_10 = code_data( "249565666", "PubChem", "09/02/2021", "Durvalumab; Imfinzi; Anti-B7H1; Monoclonal Antibody")

    # Procedures
    # None

    # Study Data
    # None

    # Activities
    # Short Name, Description, Procedures, Study Data
    study_activity_data = [
      ("BLANK", "DO NOT USE - INDEX 0", [], []),
      ("A1", "Informed Consent", [], []),
      ("A2", "Eligibility Screening", [], []),
      ("A3", "Hematology", [], []),
      ("A4", "Biochemistry", [], []),
      ("A5", "Demographics", [], []),
      ("A6", "Dosing", [], []),
      ("A7", "Plasma Biomarker", [], [])
    ]
    activities = []
    for activity in study_activity_data:
      activities.append(activity_data(*activity))
    
    # Visits
    planned_visit = code_data("C7652x", "http://www.cdisc.org", "1", "PLANNED VISIT")
    virtual_visit = code_data("C7653x", "http://www.cdisc.org", "1", "VIRTUAL VISIT")
    clinic_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')   
    hospital_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C16696')   
    in_person_mode = code_for('Encounter', 'encounterContactMode', c_code='C175574')    
    remote_audio_mode = code_for('Encounter', 'encounterContactMode', c_code='C171525')    

    # name, description, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None
    study_encounter_data = [
      ("Don't Use", "DON'T USE", None, None, None, None, None), 
      ("Screening", "SCREENING", planned_visit, clinic_setting, in_person_mode, rules[1], rules[14]),
      ("Cycle 1, Day 1", "DAY 1", planned_visit, hospital_setting, in_person_mode, rules[2], rules[15]),
      ("Cycle 1, Day 15", "DAY 15", planned_visit, hospital_setting, in_person_mode, rules[3], rules[16]),
      ("Cycle 2, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[4], rules[17]),
      ("Cycle 2, Day 15", "DAY 15",	planned_visit, hospital_setting, in_person_mode, rules[5], rules[18]),
      ("Cycle 3, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[6], rules[19]),
      ("Cycle 4, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[7], rules[20]),
      ("Cycle 5, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[8], rules[21]),
      ("Cycle 6, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[9], rules[22]),
      ("Cycle 7, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[10], rules[23]),
      ("Cycle 8, Day 1", "DAY 1",	planned_visit, hospital_setting, in_person_mode, rules[11], rules[24]),
      ("Cycle 9, Day 1", "DAY 1",	virtual_visit, clinic_setting, remote_audio_mode, rules[12], rules[25]),
      ("Follow up", "FOLLOW-UP",	planned_visit, clinic_setting, in_person_mode, rules[13], rules[26])
    ]
    encounters = []
    for encounter in study_encounter_data:
      encounters.append(encounter_data(*encounter))
    double_link(encounters, 'previousEncounterId', 'nextEncounterId')

    # Work Flow Items
    wfi_links = [
      [ encounters[2], activities[3] ], 
      [ encounters[2], activities[6] ], 
      [ encounters[2], activities[7] ], 
      [ encounters[3], activities[3] ], 
      [ encounters[3], activities[6] ], 
      [ encounters[4], activities[3] ], 
      [ encounters[4], activities[6] ], 
      [ encounters[4], activities[7] ],
      [ encounters[5], activities[3] ],
      [ encounters[5], activities[5] ],
      [ encounters[6], activities[3] ],
      [ encounters[6], activities[6] ],
      [ encounters[6], activities[7] ],
      [ encounters[7], activities[3] ], 
      [ encounters[7], activities[6] ],
      [ encounters[7], activities[7] ],
      [ encounters[8], activities[3] ],
      [ encounters[8], activities[6] ], 
      [ encounters[9], activities[3] ], 
      [ encounters[9], activities[6] ],
      [ encounters[9], activities[7] ],
      [ encounters[10], activities[3] ], 
      [ encounters[10], activities[6] ],
      [ encounters[10], activities[3] ],
      [ encounters[11], activities[6] ],
      [ encounters[11], activities[7] ],
      [ encounters[12], activities[3] ],
      [ encounters[13], activities[3] ],
      [ encounters[13], activities[4] ]
    ]
    wfis = []
    for item in wfi_links:
      wfis.append(workflow_item_data("", item[0], item[1]))
    workflow = workflow_data("Schedule of Activities", wfis)
    double_link(wfis, 'previousWorkflowItemId', 'nextWorkflowItemId')  

    # Investigational Interventions
    ii_1 = investigational_intervention_data("Olaparibstring", [code_9])
    ii_2 = investigational_intervention_data("Durvalumab", [code_8, code_10])
    ii_3 = investigational_intervention_data("AZD6738", [])
    ii = [ii_1, ii_2, ii_3]

    # Populations
    population_1 = study_design_population_data("biliary tract cancer patients who have failed to 1st-line chemotherapy")

    # Endpoints
    endpoint_1 = endpoint_data(
      "Disease control rate of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9834x", "http://www.cdisc.org", "1", "PRIMARY")
    )
    endpoint_2 = endpoint_data(
      "Disease control rate of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9834x", "http://www.cdisc.org", "1", "PRIMARY") 
    )
    endpoint_3 = endpoint_data(
      "Overall response rate of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY")
    )
    endpoint_4 = endpoint_data(
      "progression-free survival of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY")
    )
    endpoint_5 = endpoint_data(
       "duration of response of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      "PHARMACODYNAMIC",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY")
    )
    endpoint_6 = endpoint_data(
      "overall survival of response of AZD6738 + Durvalumab cohort [ Time Frame: every 12 weeks until death or up to 5 years ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_7 = endpoint_data(
      "Safety and tolerability of AZD6738 + Durvalumab cohort measured by number and grade of toxicity events [ Time Frame: through study completion, an average of 1 year ]",
      "SAFETY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_8 = endpoint_data(
      "quality of life measurement of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_9 = endpoint_data(
      "overall response rate (ORR) of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_10 = endpoint_data(
      "progression-free survival of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_11 = endpoint_data(
      "duration of response of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      "PHARMACODYNAMIC",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_12 = endpoint_data(
      "overall survival of AZD6738 + Olaparib cohort [ Time Frame: every 12 weeks until death or up to 5 years ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_13 = endpoint_data(
      "Safety and tolerability of AZD6738 + Olaparib cohort as measured by number and grade of toxicity events [ Time Frame: through study completion, an average of 1 year ]",
      "SAFETY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY") 
    )
    endpoint_14 = endpoint_data(
      "quality of life measurement of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      "EFFICACY",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY")
    )

    # Objectives
    objective_1 = objective_data(
      "To assess the effect of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients who have failed to 1st-line chemotherapy and are in second phase of disease", 
      code_data("C9844x", "http://www.cdisc.org", "1", "OBJ LEVEL"), 
      [endpoint_1, endpoint_2, endpoint_3, endpoint_4, endpoint_5, endpoint_6, endpoint_7, endpoint_8, endpoint_9, endpoint_10, endpoint_11, endpoint_12, endpoint_13, endpoint_14]
    )
    objective_2 = objective_data(
      "To assess the effect of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients who have failed to 1st-line chemotherapy and are in second phase of disease", 
      code_data("C9844x", "http://www.cdisc.org", "1", "OBJ LEVEL"), 
      [endpoint_7, endpoint_13]
    )
    objective_3 = objective_data(
      "To assess the effect of AZD6738 and Durvalumab combination or AZD6738 and Olaparib combination in biliary tract cancer patients who have failed to 1st-line chemotherapy", 
      code_data("C9844x", "http://www.cdisc.org", "1", "OBJ LEVEL"), 
      [endpoint_1, endpoint_2, endpoint_3, endpoint_4, endpoint_5, endpoint_6, endpoint_7, endpoint_8, endpoint_9, endpoint_10, endpoint_11, endpoint_12, endpoint_14]
    )
    objectives = [objective_1, objective_2, objective_3]

    # Indications
    indication_1 = study_indication_data("Bile duct cancer", [code_4, code_5, code_6])
    indication_2 = study_indication_data("Influenza", [code_1, code_2, code_3])
    indications = [indication_1, indication_2]

    # Intercurrent Events
    i_event_1 = intercurrent_event_data(
     "Intercurrent Event 1", 
     "An Intercuurent Event that could happen in a study", 
     "A very bold strategy"
    )

    # Estimands
    population_2 = analysis_population_data("The analysis population")
    estimand_1 = estimand_data("Measure 1", population_2, ii_1, endpoint_1, [i_event_1])
    estimands = [estimand_1]

    # Study Arms
    origin_type = code_data("C6574y", "http://www.cdisc.org", "1", "SUBJECT DATA")
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    study_arm_1 = study_arm_data("DURVALUMAB ADD_ON", "AZD6738 + Durvalumab", treatment, "Captured subject data", origin_type)
    study_arm_2 = study_arm_data("OLAPARIB_ADDON", "AZD6738 + Olaparib", treatment, "Captured subject data", origin_type)

    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    screening = code_for('StudyEpoch', 'studyEpochType', submission_value='SCREENING') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    study_epoch_1 = study_epoch_data("SCREEN", 	"Screening",screening, [ encounters[1]])
    study_epoch_2 = study_epoch_data("RUN-IN", "Run-In", run_in, [ encounters[2], encounters[3], encounters[4]])
    study_epoch_3 = study_epoch_data("TREATMENT 1", "Treatment Cycle 1", treatment, [ encounters[5], encounters[6], encounters[7]])
    study_epoch_4 = study_epoch_data("TREATMENT 2", "Treatment Cycle 2", treatment, [ encounters[8], encounters[9]])
    study_epoch_5 = study_epoch_data("TREATMENT X", "Treatment Cycle X", treatment, [ encounters[10], encounters[11]])
    study_epoch_6 = study_epoch_data("FOLLOW-UP", "Follow-up", follow_up, [ encounters[12], encounters[13]])
    epochs = [study_epoch_1, study_epoch_2, study_epoch_3, study_epoch_4, study_epoch_5, study_epoch_6]
    double_link(epochs, 'previousEpochId', 'nextEpochId')
    print(epochs)

    study_element_1 = study_element_data("SCREENING", "Screening", rules[1], rules[2])
    study_element_2 = study_element_data("AZD_DRUV", "AZD6738 + Durvalumab", rules[1], rules[1])
    study_element_3 = study_element_data("AZD_OLA", "AZD6738 + Olaparib", rules[1], rules[1])
    study_element_4 = study_element_data("FOLLOW-UP", "Follow-up", rules[1], rules[1])
    study_element_5 = study_element_data("FOLLOW-UP", "Follow-up", rules[1], rules[1])
    study_element_6 = study_element_data("FOLLOW-UP", "Follow-up", rules[1], rules[1])

    study_cells = []
    study_cells.append(study_cell_data(study_arm_1, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_2, [study_element_2]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_3, [study_element_3]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_4, [study_element_4]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_5, [study_element_5]))
    study_cells.append(study_cell_data(study_arm_1, study_epoch_6, [study_element_6]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_1, [study_element_1]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_2, [study_element_2]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_3, [study_element_3]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_4, [study_element_4]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_5, [study_element_5]))
    study_cells.append(study_cell_data(study_arm_2, study_epoch_6, [study_element_6]))

    intent = code_for('StudyDesign', 'trialIntentType', c_code='C15714')
    design_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='PARALLEL')

    design_1 = study_design_data([intent], design_type, int_model, study_cells, indications, objectives, [population_1], ii, [workflow], estimands)
    designs = [design_1]

    # Protocol versions    
    final = code_data("C1113x", "http://www.cdisc.org", "1", "FINAL")
    protocol_version_1 = study_protocol_version_data(
      "DDR", 
      "Targeting Agents in ABTC", 
      "DDR-Umbrella Study of DDR (DNA-Damage Response) Targeting Agents in Advanced Biliary Tract Cancer Umbrella ABTC Study",
      "DDR-Umbrella Study of DNA-Damage Response Targeting Agents in Advanced Biliary Tract Cancer",
      "", 
      None, 
      "2022-01-01", 
      final
    )
    protocol_versions = [protocol_version_1]

    # Study Identifiers
    phase = code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase II Trial")
    study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
    registry_type = code_data("C2365x", "http://www.cdisc.org", "1", "REGISTRY_STUDY_IDENTIFIER")
    sponsor_type = code_data("C2365y", "http://www.cdisc.org", "1", "SPONSOR_STUDY_IDENTIFIER")
    organisation_1 = organization_data("DUNS", "123456789", "ACME Pharma", sponsor_type)
    organisation_2 = organization_data("USGOV", "CT-GOV", "ClinicalTrials.gov", registry_type)
    identifier_1 = study_identifier_data("NCT04298021", organisation_2)
    identifier_2 = study_identifier_data("NCT04298023", organisation_2)
    identifier_3 = study_identifier_data("AP002020202", organisation_1)
    identifiers = [identifier_1, identifier_2, identifier_3]

    # Assemble complete study
    study_title = "Umbrella Study of DDR (DNA-Damage Response) Targeting Agents in Advanced Biliary Tract Cancer"
    return study_data(study_title, "1", study_type, phase, identifiers, protocol_versions, designs)

