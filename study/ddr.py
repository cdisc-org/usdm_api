from factory.factory import *

class DDR():

  def json():

    # Rules
    rule_01 = transition_rule_data("6 weeks prior to start treatment")
    rule_02 = transition_rule_data("Start of treatment")
    rule_03 = transition_rule_data("Start of treatment")
    rule_04 = transition_rule_data("End of last treatment day")
    rule_05 = transition_rule_data("Start of treatment",)
    rule_06 = transition_rule_data("End of last treatment day",)
    rule_07 = transition_rule_data("End of last treatment day",)
    rule_08 = transition_rule_data("Last follow-up measurement",)
    rule_09 = transition_rule_data("-D5")
    rule_10 = transition_rule_data("-D3")
    rule_11 = transition_rule_data("-D1")
    rule_12 = transition_rule_data("D1")
    rule_13 = transition_rule_data("D3")
    rule_14 = transition_rule_data("D5")
    rule_15 = transition_rule_data("D1")
    rule_16 = transition_rule_data("D3")
    rule_17 = transition_rule_data("D1")
    rule_18 = transition_rule_data("D4")
    rule_19 = transition_rule_data("W2")
    rule_20 = transition_rule_data("W6")
    rule_21 = transition_rule_data("-D5")
    rule_22 = transition_rule_data("-D3")
    rule_23 = transition_rule_data("-D1")
    rule_24 = transition_rule_data("D1")
    rule_25 = transition_rule_data("D3")
    rule_26 = transition_rule_data("D5")
    rule_27 = transition_rule_data("D1")
    rule_28 = transition_rule_data("D3")
    rule_29 = transition_rule_data("D1")
    rule_30 = transition_rule_data("D4")
    rule_31 = transition_rule_data("W2")
    rule_32 = transition_rule_data("W6")

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
    dummy_procedure = code_data("C4936x", "http://www.cdisc.org", "1", "DUMMY PROCEDURE")
    procedure_1 = procedure_data("Remote ICF collection", dummy_procedure)
    procedure_2 = procedure_data("Blood sample collection", dummy_procedure)
    procedure_3 = procedure_data("Blood sample analysis",dummy_procedure)
    procedure_4 = procedure_data("Drug administration", dummy_procedure)
    procedure_5 = procedure_data("Hospitalisation", dummy_procedure)
    procedure_6 = procedure_data("Weight measurement", dummy_procedure)

    #Study Data
    study_data_1 = study_data_data("ALAT", "Alanine transaminase", "https://www.dropbox.com/s/84quxhfj254k2sh/LB_LOCAL_XML.xml?dl=1")
    study_data_2 = study_data_data("ASAT", "Aspartate aminotransferase", "")
    study_data_3 = study_data_data("ERY", "Erythrocytes", "")
    study_data_4 = study_data_data("WBC", "White blood cell count", "")
    study_data_5 = study_data_data("DOSDATE", "Date of investigational drug administration", "")
    study_data_6 = study_data_data("WGHT", "Weight", "https://www.dropbox.com/s/b2mfhiri5a5z34t/weight.yaml?dl=1")
    study_data_7 = study_data_data("AGE", "Age", "https://www.dropbox.com/s/7m1vxxxauxe0c97/DM_XML.xml?dl=1")
    study_data_8 = study_data_data("OAS", "Oncology Assessment Scale", "")
    study_data_9 = study_data_data("DPS", "Disease Progression Scale", "")
    study_data_10 = study_data_data("TSO", "Time since onset", "")
    study_data_11 = study_data_data("HGT", "Height", "https://www.dropbox.com/s/42dhfj2ani8rfjd/height.yaml?dl=1")
    study_data_12 = study_data_data("QTc", "QTc interval", "")
    study_data_13 = study_data_data("ST", "St-segment", "")
    study_data_14 = study_data_data("WBC_DIP", "WBC dipstick", "")
    study_data_15 = study_data_data("HCG", "Serum HCG", "")
    study_data_16 = study_data_data("SBP", "Systolic blood pressure", "")
    study_data_17 = study_data_data("DBP", "Diastolic Blood Pressure", "")

    # Activities
    activity_1 = activity_data("IC", "Informed consent", 1, [procedure_1], [])
    activity_2 = activity_data("EC", "Eligibility criteria", 2, [], [])
    activity_3 = activity_data("DM", "Demography", 3, [], [study_data_7])
    activity_4 = activity_data("MH", "Medical history", 4, [], [])
    activity_5 = activity_data("DC", "Disease characteristics", 5, [], [study_data_8, study_data_10])
    activity_6 = activity_data("PE", "Physical exam", 6, [], [])
    activity_7 = activity_data("VS1", "Height", 7, [], [study_data_11])
    activity_8 = activity_data("ECG", "12-lead ECG", 8, [], [study_data_12, study_data_13])
    activity_9 = activity_data("LB1", "Hematology (predose)", 9, [procedure_2, procedure_3], [study_data_3, study_data_4])
    activity_10 = activity_data("LB2", "Chemistry (predose)", 10, [procedure_2, procedure_3], [study_data_1, study_data_2])
    activity_11 = activity_data("LB3", "Serology", 11, [], [])
    activity_12 = activity_data("LB4", "Urinalysis", 12, [], [study_data_14])
    activity_13 = activity_data("PREG", "Pregnancy test", 13, [], [study_data_15])
    activity_14 = activity_data("EX", "Ensure availability of medication X", 14, [], [study_data_5])
    activity_15 = activity_data("HO", "Hospitalization", 15, [procedure_5], [])
    activity_16 = activity_data("VS2", "Weight", 16, [procedure_6], [study_data_6])
    activity_17 = activity_data("VS3", "Vital signs", 17, [], [study_data_16, study_data_17])
    activity_18 = activity_data("AE", "adverse events", 18, [], [])
    activity_19 = activity_data("CM", "Concomitant medications", 19, [], [])

    # Visits
    planned_visit = code_data("C7652x", "http://www.cdisc.org", "1", "PLANNED VISIT")
    virtual_visit = code_data("C7653x", "http://www.cdisc.org", "1", "VIRTUAL VISIT")
    clinic_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')   
    hospital_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C16696')   
    in_person_mode = code_for('Encounter', 'encounterContactMode', c_code='C175574')    
    remote_audio_mode = code_for('Encounter', 'encounterContactMode', c_code='C171525')    

    encounter_1_activities = [
      activity_1, 
      activity_2, 
      activity_3, 
      activity_4, 
      activity_5, 
      activity_6, 
      activity_7, 
      activity_8, 
      activity_9, 
      activity_10,
      activity_11,
      activity_12,
      activity_13,
      activity_16,
      activity_17
    ]
    encounter_2_activities = [
      activity_8, 
      activity_11,
      activity_15,
      activity_17
    ]
    encounter_3_activities = [
      activity_6, 
      activity_8, 
      activity_11,
      activity_17
    ]
    encounter_4_activities = [
      activity_8, 
      activity_9,
      activity_10,
      activity_11,
      activity_12,
      activity_13,
      activity_17
    ]
    encounter_5_activities = [
      activity_11,
      activity_14,
      activity_15,
      activity_16,
      activity_17
    ]
    encounter_8_activities = [
      activity_11,
      activity_14,
      activity_15,
      activity_16,
      activity_17
    ]
    encounter_6_7_9_11_activities = [
      activity_17
    ]
    encounter_10_activities = [
      activity_11,
      activity_14,
      activity_15,
      activity_17
    ]
    encounter_12_activities = [
      activity_6,
      activity_8,
      activity_9,
      activity_10,
      activity_11,
      activity_12,
      activity_16,
      activity_17
    ]	
    encounter_13_activities = []

    encounter_1 = encounter_data("SCREENING VISIT", "", 1, planned_visit, clinic_setting, in_person_mode, encounter_1_activities)
    encounter_2 = encounter_data("RUN-IN VISIT 1", "", 2, planned_visit, hospital_setting, in_person_mode, encounter_2_activities, rule_09, rule_21)
    encounter_3 = encounter_data("RUN-IN VISIT 2", "", 3, planned_visit, hospital_setting, in_person_mode, encounter_3_activities, rule_10, rule_22)
    encounter_4 = encounter_data("RUN-IN VISIT 3", "", 4, planned_visit, hospital_setting, in_person_mode, encounter_4_activities, rule_11, rule_23)
    encounter_5 = encounter_data("CYCLE 1, TREATMENT DAY 1", "", 5, planned_visit, hospital_setting, in_person_mode, encounter_5_activities, rule_12, rule_24)
    encounter_6 = encounter_data("CYCLE 1, TREATMENT DAY 3", "", 6, planned_visit, hospital_setting, in_person_mode, encounter_6_7_9_11_activities, rule_13, rule_25)
    encounter_7 = encounter_data("CYCLE 1, TREATMENT DAY 5", "", 7, planned_visit, hospital_setting, in_person_mode, encounter_6_7_9_11_activities, rule_14, rule_26)
    encounter_8 = encounter_data("CYCLE 2, TREATMENT DAY 1", "", 8, planned_visit, clinic_setting, in_person_mode, encounter_8_activities, rule_15, rule_27)
    encounter_9 = encounter_data("CYCLE 2, TREATMENT DAY 3", "", 9, planned_visit, hospital_setting, in_person_mode, encounter_6_7_9_11_activities, rule_16, rule_28)
    encounter_10 = encounter_data("CYCLE X, TREATMENT DAY 1", "", 10, planned_visit, hospital_setting, in_person_mode, encounter_10_activities, rule_17, rule_29)
    encounter_11 = encounter_data("CYCLE X, TREATMENT DAY 4", "", 11, planned_visit, hospital_setting, in_person_mode, encounter_6_7_9_11_activities, rule_18, rule_30)
    encounter_12 = encounter_data("FU 1", "", 12, planned_visit, clinic_setting, in_person_mode, encounter_12_activities, rule_19, rule_31)
    encounter_13 = encounter_data("FU 2", "", 13, virtual_visit, clinic_setting, remote_audio_mode, encounter_13_activities, rule_20, rule_32)
	
    # Investigational Interventions
    ii_1 = investigational_intervention_data("Olaparibstring", "done", [code_9])
    ii_2 = investigational_intervention_data("Durvalumab", "done", [code_8, code_10])
    ii_3 = investigational_intervention_data("AZD6738", "done", [])
    ii = [ii_1, ii_2, ii_3]

    # Populations
    population_1 = population_data("biliary tract cancer patients who have failed to 1st-line chemotherapy")

    # Estimands
    estimand_1 = estimand_data("Measure 1", population_1)

    # Intercurrent Events
    #i_event_1 = intercurrent_event_data(
    #  "Intercurrent Event 1", 
    #  "An Event", 
    #  [ 
    #    code_data("C9822x", "http://www.cdisc.org", "1", "IE1"), 
    #    code_data("C9822y", "http://www.cdisc.org", "1", "IE2")
    #  ]
    #)

    # Endpoints
    endpoint_1 = endpoint_data(
      "Disease control rate of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9834x", "http://www.cdisc.org", "1", "PRIMARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_2 = endpoint_data(
      "Disease control rate of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9834x", "http://www.cdisc.org", "1", "PRIMARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_3 = endpoint_data(
      "Overall response rate of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_4 = endpoint_data(
      "progression-free survival of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_5 = endpoint_data(
       "duration of response of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9835y", "http://www.cdisc.org", "1", "PHARMACODYNAMIC")
    )
    endpoint_6 = endpoint_data(
      "overall survival of response of AZD6738 + Durvalumab cohort [ Time Frame: every 12 weeks until death or up to 5 years ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_7 = endpoint_data(
      "Safety and tolerability of AZD6738 + Durvalumab cohort measured by number and grade of toxicity events [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "SAFETY")
    )
    endpoint_8 = endpoint_data(
      "quality of life measurement of AZD6738 + Durvalumab cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_9 = endpoint_data(
      "overall response rate (ORR) of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_10 = endpoint_data(
      "progression-free survival of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_11 = endpoint_data(
      "duration of response of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9835y", "http://www.cdisc.org", "1", "PHARMACODYNAMIC")
    )
    endpoint_12 = endpoint_data(
      "overall survival of AZD6738 + Olaparib cohort [ Time Frame: every 12 weeks until death or up to 5 years ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
    )
    endpoint_13 = endpoint_data(
      "Safety and tolerability of AZD6738 + Olaparib cohort as measured by number and grade of toxicity events [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "SAFETY")
    )
    endpoint_14 = endpoint_data(
      "quality of life measurement of AZD6738 + Olaparib cohort [ Time Frame: through study completion, an average of 1 year ]",
      code_data("C9835x", "http://www.cdisc.org", "1", "SECONDARY"), 
      code_data("C9834y", "http://www.cdisc.org", "1", "EFFICACY")
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
    study_epoch_1 = study_epoch_data("SCREEN", 	"Screening", 1, screening)
    study_epoch_2 = study_epoch_data("RUN-IN", "Run-In", 2, run_in)
    study_epoch_3 = study_epoch_data("TREATMENT 1", "Treatment Cycle 1", 3, treatment)
    study_epoch_4 = study_epoch_data("TREATMENT 2", "Treatment Cycle 2", 4, treatment)
    study_epoch_5 = study_epoch_data("TREATMENT X", "Treatment Cycle X", 5, treatment)
    study_epoch_6 = study_epoch_data("FOLLOW-UP", "Follow-up", 6, follow_up)

    study_element_1 = study_element_data("SCREENING", "Screening", [encounter_1], [], rule_01, rule_05)
    study_element_2 = study_element_data("AZD_DRUV", "AZD6738 + Durvalumab", [encounter_2, encounter_3, encounter_4], [], rule_02, rule_06)
    study_element_3 = study_element_data("AZD_OLA", "AZD6738 + Olaparib", [encounter_5, encounter_6, encounter_7], [], rule_03, rule_07)
    study_element_4 = study_element_data("FOLLOW-UP", "Follow-up", [encounter_8, encounter_9], [], rule_04, rule_08)
    study_element_5 = study_element_data("FOLLOW-UP", "Follow-up", [encounter_10, encounter_11], [], rule_04, rule_08)
    study_element_6 = study_element_data("FOLLOW-UP", "Follow-up", [encounter_12, encounter_13], [], rule_04, rule_08)

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

    design_1 = study_design_data([intent], design_type, study_cells, indications, objectives, [population_1], ii, [])
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

