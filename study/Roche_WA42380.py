from factory.factory import *

class RocheWA42380():

  def json():

    # <<<<< Visit Rules need adding >>>>>
    # Rules
    study_rule_data = [
      # Element Start Rules
      "Informed consent",
      "First dose of a treatment epoch, where the does is XXX",
      "First dose of a treatment epoch, where the does is placebo",
      "28 days after first dose of the previous treatment epoch",

      # Element Start Rules
      # Index 4, zero based.
      "As soon as possibe once screening is complete",
      "After 28 days, where the does is XXX",
      "After 28 days, where the does is XXX",
      "After day 60",

    ]

    rules = []
    for rule in study_rule_data:
      rules.append(transition_rule_data(rule))

    # <<<<< To be added >>>>>
    # Procedures

    # <<<<< More to be added >>>>>
    # Study Data
    raw_study_data = [
      # Chemistry
      ( "bicarbonate", "bicarbonate", "" ),
      ( "total carbon dioxide", "total carbon dioxide", "" ),
      ( "sodium	sodium", "" ),
      ( "potassium", "potassium", "" ),
      ( "chloride", "chloride", "" ),
      ( "glucose", "glucose", "" ),
      ( "BUN", "Blood urea nitrogen", "" ),
      ( "Urea", "Urea", "" ),
      ( "creatinine", "creatinine", "" ),
      ( "total protein", "total protein", "" ),
      ( "albumin	albumin", "" ),
      ( "phosphorus", "phosphorus", "" ),
      ( "calcium", "calcium", "" ),
      ( "total bilirubin", "total bilirubin", "" ),
      ( "ALP", "Alkaline Phosphatase, """ ),
      ( "ALT", "Alanine Transaminase, """ ),
      ( "AST", "Aspartate Aminotransferase", "" ),
      ( "uric acid", "uric acid", "" ),
      ( "LDH", "Lactate Dehydrogenase", "" ),
      ( "ferritin", "ferritin", "" ),
      ( "D-dimer", "D-dimer", "" ),

      # Hematology (index 21, 0 based)
      ( "RBC", "Red Blood Cell count", "" ),
      ( "HCT", "Hematocrit", "" ),
      ( "WBC", "White blood Cell count", "" ),
      ( "Hemoglobin", "Hemoglobin", ""),
      ( "platelet count", "platelet count", ""),
      ( "", "differential count (neutrophils, eosinophils, basophils, monocytes, lymphocytes)", ""),
      ( "", "lymphocyte subsets (T cells, B cells, and NK cells)", ""),

      # Vital Signs (28)
      ( "Respiratory rate", "respiratory rate", ""),
      ( "Pulse rate", "pulse rate", ""),
      ( "Systolic blood pressure" "sysolic blodd pressure", ""),
      ( "Diastolic blood pressures", "diastolic blood pressures", ""),
      ( "Body temperature, ", "body temperature", ""),
      ( "Oxygen saturation", "oxygen saturation", ""),
      ( "NEWS2", "National Early Warning Score 2", ""),
      
      #DM (35)
      ( "Weight", "Weight", "" ),

    ]
    study_data_items = []
    for data in raw_study_data:
      study_data_items.append(study_data_data(*data))

    # <<<<< Activities need linking to SD and Procedures >>>>>
    # Activities
    # Short Name, Description, Procedures, Study Data
    study_activity_data = [
      ("Informed consent", "Informed consent", [], []),
      ("Inclusion/exclusion criteria", "Inclusion/exclusion criteria", [], []),
      ("Demographic data", "Demographic data", [], []),
      ("Randomization", "Randomization", [], []),
      ("Medical history", "Medical history", [], []),
      ("Complete physical examination", "Complete physical examination", [], []),
      ("Weight", "Weight", [], []),
      ("COVID-19 diagnosis", "COVID-19 diagnosis", [], []),
      ("Chest X-ray/CT scan", "Chest X-ray/CT scan", [], []),
      ("ECG", "Electrocardiogram", [], []),
      ("Pregnancy test", "Pregnancy test", [], []),
      ("PaO2/FiO2", "arterial oxygen partial pressure/fraction of inspired oxygen", [], []),
      ("SpO2", "peripheral capillary oxygen saturation", [], []),
      ("Vital signs", "Vital signs", [], []),
      ("Ordinal scoring", "Ordinal scoring", [], []),
      ("Adverse events", "Adverse events", [], []),
      ("Concomitant medications", "Concomitant medications", [], []),
      ("Hematology", "Hematology", [], []),
      ("Chemistry", "Chemistry", [], []),
      ("Study drug administration", "Study drug administration", [], []),
      ("Central Labs", "Central Labs", [], []),
      ("Serum PD (CRP, IL-6, sIL-6R)", "", [], []),
      ("Serum PK", "Serum pharmacokinetic", [], []),
      ("Serum sample for exploratory biomarkers", "Serum sample for exploratory biomarkers", [], []),
      ("SARS-CoV-2 viral load", "SARS-CoV-2 viral load", [], []),
      ("Serum SARS-CoV-2 antibody titer", "Serum SARS-CoV-2 antibody titer", [], []),
      ("Cryopreserved PBMCs", "Cryopreserved peripheral blood mononuclear cells", [], []),
      ("Whole blood in PAXgene tubes for RNA analyses", "", [], []),
    ]
    activities = []
    for activity in study_activity_data:
      activities.append(activity_data(*activity))
    double_link(activities, 'previousActivityId', 'nextActivityId')

    # Visits
    # Codes
    a_visit = code_for('Encounter', 'encounterType', submission_value='Visit')   
    clinic_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')   
    hospital_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C16696')   
    in_person_mode = code_for('Encounter', 'encounterContactMode', c_code='C175574')    
    remote_audio_mode = code_for('Encounter', 'encounterContactMode', c_code='C171525')    
    # Fields: name, description, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None
    study_encounter_data = [
      ("Screening", "SCREENING", a_visit, clinic_setting, in_person_mode, None, None),
      ("Baseline", "BASELINE", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 1", "Day 1", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 2A", "Day 2A", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 2B", "Day 2B", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 3", "Day 3", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 4", "Day 4", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 5", "Day 5", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 6", "Day 6", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 7", "Day 7", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 8", "Day 8", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 9", "Day 9", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 10", "Day 10", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 11", "Day 11", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 12", "Day 12", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 13", "Day 13", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 14", "Day 14", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 15", "Day 15", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 16", "Day 16", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 17", "Day 17", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 18", "Day 18", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 19", "Day 19", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 20", "Day 20", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 21", "Day 21", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 22", "Day 22", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 23", "Day 23", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 24", "Day 24", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 25", "Day 25", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 26", "Day 26", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 27", "Day 27", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 28", "Day 28", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 35", "Day 35", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 45", "Day 45", a_visit, hospital_setting, in_person_mode, None, None),
      ("Day 60", "Day 60", a_visit, hospital_setting, in_person_mode, None, None)
    ]

    encounters = []
    for encounter in study_encounter_data:
      encounters.append(encounter_data(*encounter))
    double_link(encounters, 'previousEncounterId', 'nextEncounterId')

    
    # <<<<< Need setting up >>>>>
    # Work Flow Items
    wfi_links = [
      [ encounters[0], activities[0] ], 
      [ encounters[0], activities[1] ], 
      [ encounters[0], activities[2] ], 
      [ encounters[1], activities[2] ], 
      [ encounters[1], activities[5] ], 
      [ encounters[1], activities[6] ], 
      [ encounters[1], activities[7] ], 
      [ encounters[2], activities[2] ], 
      [ encounters[2], activities[5] ], 
      [ encounters[3], activities[2] ], 
      [ encounters[3], activities[5] ], 
      [ encounters[3], activities[6] ],
      [ encounters[3], activities[7] ],
      [ encounters[4], activities[2] ],
      [ encounters[4], activities[5] ],
      [ encounters[5], activities[2] ],
      [ encounters[5], activities[5] ],
      [ encounters[5], activities[6] ],
      [ encounters[6], activities[2] ], 
      [ encounters[6], activities[3] ],
      [ encounters[6], activities[4] ],
      [ encounters[6], activities[7] ],
      [ encounters[7], activities[2] ],
      [ encounters[7], activities[5] ], 
      [ encounters[8], activities[2] ], 
      [ encounters[8], activities[5] ],
      [ encounters[8], activities[6] ],
      [ encounters[8], activities[7] ],
      [ encounters[9], activities[2] ], 
      [ encounters[9], activities[3] ],
      [ encounters[9], activities[4] ],
      [ encounters[10], activities[2] ],
      [ encounters[10], activities[5] ],
      [ encounters[10], activities[7] ],
      [ encounters[11], activities[2] ],
      [ encounters[11], activities[5] ],
      [ encounters[11], activities[6] ],
      [ encounters[12], activities[2] ],
      [ encounters[12], activities[3] ],
      [ encounters[12], activities[4] ],
      [ encounters[13], activities[2] ],
      [ encounters[13], activities[5] ],
      [ encounters[14], activities[2] ],
      [ encounters[14], activities[5] ],
      [ encounters[14], activities[6] ],
      [ encounters[15], activities[2] ], 
      [ encounters[15], activities[3] ],
      [ encounters[15], activities[4] ],
      [ encounters[16], activities[2] ],
      [ encounters[16], activities[5] ],
      [ encounters[17], activities[2] ],
      [ encounters[17], activities[5] ],
      [ encounters[17], activities[6] ],
      [ encounters[18], activities[2] ],
      [ encounters[18], activities[3] ],
      [ encounters[18], activities[4] ]
    ]
    wfis = []
    for item in wfi_links:
      wfis.append(workflow_item_data("", item[0], item[1]))
    workflow = workflow_data("Workflow 1", wfis)
    double_link(wfis, 'previousWorkflowItemId', 'nextWorkflowItemId')  

    # <<<<< Need setting up >>>>>
    # Investigational Interventions
    ii_code_1 = code_data( "XX031ZA", "ATC", "2021", "SubstX")
    ii_1 = investigational_intervention_data("Treatment with substX", [ii_code_1])
    ii = [ii_1]
						
    # <<<<< Need setting up >>>>>
    # Study Populations
    study_population_1 = study_design_population_data("A metastatic cancer population")

    # <<<<< Need setting up >>>>>
    # Endpoints
    primary_endpoint = code_for('Endpoint', 'endpointLevel', submission_value='Primary Endpoint')
    endpoint_1 = endpoint_data(
      "Survival rate after cycle 8 of treatment",
      "EFFICACY",
      primary_endpoint
    )

    # <<<<< Need setting up >>>>>
    # Objectives
    primary_objective = code_for('Objective', 'objectiveLevel', submission_value='Study Primary Objective')
    objective_1 = objective_data(
      "Evaluate sensitivity index from baseline to end of study (16 weeks)", 
      primary_objective, 
      [endpoint_1]
    )
    objectives = [objective_1]

    # <<<<< Need setting up >>>>>
    # Indications
    # Codes
    code_1 = code_data( "E11", "ICD-10-CM", "10", "Type 2 diabetes mellitus")
    code_2 = code_data( "44054006", "SNOMED", "2022", "Diabetes mellitus type 2 (disorder)"	)
    code_3 = code_data( "E10", "ICD-10-CM", "10", "Type 1 diabetes mellitus")
    code_4 = code_data( "44635009", "SNOMED", "2022", "Diabetes mellitus type 1 (disorder)"	)
    indication_1 = study_indication_data("Diabetes Type II", [code_1, code_2])
    indication_2 = study_indication_data("Diabetes Type I", [code_3, code_4])
    indications = [indication_1, indication_2]

    # <<<<< Need setting up >>>>>
    # Intercurrent Events
    i_event_1 = intercurrent_event_data(
      "Termination", 
      "Termination",
      "Patients with out of range lab values before dosing will be excluded"
    )
    i_event_2 = intercurrent_event_data(
      "Missed dose",
      "Missed dose",
      "Patients with 1 missed dose will be included. Patients with >1 missed dose will be excluded"
    )
    i_event_3 = intercurrent_event_data(
      "Termination",
      "Termination",
      "Patients with out of range lab values before dosing will be excluded"
    )
    i_event_4 = intercurrent_event_data(
      "Out of range lab values",
      "Out of range lab values",
      "Patients with out of range lab values before dosing will be excluded"
    )

    # <<<<< Need setting up >>>>>
    # Analysis Populations
    analysis_population_1 = analysis_population_data("ITT")
    analysis_population_2 = analysis_population_data("PP")

    # <<<<< Need setting up >>>>>
    # Estimands
    estimand_1 = estimand_data("Measure 1", analysis_population_1, ii_1, endpoint_1, [i_event_1])
    estimand_2 = estimand_data("Measure 2", analysis_population_2, ii_1, endpoint_1, [i_event_2, i_event_3, i_event_4])
    estimands = [estimand_1, estimand_2]

    # Study Arms
    # Codes
    origin_type = code_for('StudyArm', 'studyArmDataOriginType', submission_value='Data Generated Within Study') 
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    # Fields: name, description, arm_type, origin_description, origin_type
    study_arm_1 = study_arm_data("TCZ+SOC", "Tocilizumab with SOC", treatment, "Captured subject data", origin_type)
    study_arm_2 = study_arm_data("Placebo+SOC", "Palcebo with SOC", placebo, "Captured subject data", origin_type)

    # <<<<< Links to encounters need setting up >>>>>
    # Epochs
    # Codes
    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    screening = code_for('StudyEpoch', 'studyEpochType', submission_value='SCREENING') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    # Fields: name, description, epoch_type, encounters
    raw_epoch_data = [
      ("Screening", "Screening", screening, [encounters[0]]),
      ("Treatment", "Treatment", treatment, [ encounters[14], encounters[15], encounters[16], encounters[17] ]),
      ("Follow-up", "Follow-up", follow_up, [ encounters[18] ])
    ]
    epochs = []
    for epoch in raw_epoch_data:
      epochs.append(study_epoch_data(*epoch))
    double_link(epochs, 'previousStudyEpochId', 'nextStudyEpochId')

    # <<<<< Rules need updatting >>>>>
    # Elements
    # Fields: name, description, start rule, end rule
    raw_element_data = [
      ("Screening", "Screening", rules[35], rules[40]),
      ("Treatment", "Tocilizumab in combination with standard of care", rules[36], rules[41]),
      ("Palcebo", "Placebo in combination with standard of care", rules[39], rules[44]),
      ("Follow Up", "Follow up", None, None),
    ]
    elements = []
    for element in raw_element_data:
      elements.append(study_element_data(*element))

    # Study Cells
    study_cells = []
    study_cells.append(study_cell_data(study_arm_1, epochs[0], [ elements[0] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[1], [ elements[1] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[2], [ elements[3] ]))
    study_cells.append(study_cell_data(study_arm_2, epochs[0], [ elements[0] ]))
    study_cells.append(study_cell_data(study_arm_2, epochs[1], [ elements[2] ]))
    study_cells.append(study_cell_data(study_arm_2, epochs[2], [ elements[3] ]))

    # <<<<< Need setting up >>>>>
    # Study Design
    intent = code_for('StudyDesign', 'trialIntentType', submission_value='CURE')
    design_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='SEQUENTIAL')
    design_1 = study_design_data([intent], design_type, int_model, study_cells, indications, objectives, [study_population_1], ii, [workflow], estimands)
    designs = [design_1]

    # Protocol versions
    # Fields: brief_title, official_title, public_title, scientific_title, version, amendment, effective_date, status):
    draft_status = code_for('StudyProtocolVersion', 'protocolStatus', submission_value='Draft')
    protocol_version_1 = study_protocol_version_data(
      "COVACTA", 
      "A Study to Evaluate the Safety and Efficacy of Tocilizumab in Patients With Severe COVID-19 Pneumonia", 
      "",
      "",
      "3", 
      None, 
      "2020-06-11", 
      draft_status
    )
    protocol_versions = [protocol_version_1]

    # Study Identifiers
    registry_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Registry')
    sponsor_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Sponsor')
    regulator_type = code_for('Organization', 'organizationType', submission_value='Regulatory Agency')
    organisation_1 = organization_data("DUNS", "482242971", "F. Hoffmann-la Roche Ag", sponsor_type)
    organisation_2 = organization_data("USGOV", "CT-GOV", "ClinicalTrials.gov", registry_type)
    organisation_3 = organization_data("EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database", regulator_type)
    identifier_1 = study_identifier_data("WA42380", organisation_1)
    identifier_2 = study_identifier_data("NCT04320615", organisation_2)
    identifier_3 = study_identifier_data("2020-001154-22", organisation_3)
    identifiers = [identifier_1, identifier_2, identifier_3]

    # Assemble complete study
    study_title = "TCZ"
    phase = code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase III Trial")
    study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
    return study_data(study_title, "1", study_type, phase, identifiers, protocol_versions, designs)

