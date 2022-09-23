from factory.factory import *

class BMS():

  def json():

    # Rules
    study_rule_data = [
      # Visit Start Rules
      "6 weeks prior to treatment",
      "2 hours before treatment",
      "2 hours before treatment",
      "start of day 8",
      "start of day 15",
      "start of day 22",
      "start of day 29",
      "start of day 36",
      "start of day 43",
      "start of day 50",
      "start of day 57",
      # Index (from 0) 11
      "start of day 64",
      "start of day 71",
      "start of day 78",
      "start of day 85",
      "start of day 92",
      "start of day 99",
      "start of day 106",

      # Visit End Rules
      # 18
      "start of run-in period",
      "end of day 1",
      "end of day 14",
      "end of day 21",
      "end of day 28",
      "end of day 35",
      "end of day 42",
      "end of day 49",
      "end of day 56",
      "end of day 63",
      "end of day 70",
      "end of day 77",
      # 30
      "end of day 84",
      "end of day 91",
      "end of day 99",
      "end of day 105",
      "end of day 112",

      # Element Start Rules
      # 35
      "6 weeks prior to treatment",
      "Start of Week 1",
      "Start of Week 5",
      "Start of Week 9",
      "Start of Week 13",
				
      # Element End Rules
      # 40
      "Start of run-in period",
      "End of Week 4",
      "End of Week 8",
      "End of Week 12",
      "End of Week 16"
    ]

    rules = []
    for rule in study_rule_data:
      rules.append(transition_rule_data(rule))

    # Procedures
    # None

    # Study Data
    raw_study_data = [
      #Heam
      ( "RBC", "Red Blood Cell count", "" ),
      ( "HCT", "Hematocrit", "" ),
      ( "WBC", "White blood Cell differential", "" ),

      #Bio
      ( "CHOL",	"Cholesterol", "" ),
      ( "MG", "Magnesium", "" ),
      ( "P", "Potassium", "" ),

      #DM
      ( "HGT", "Height", "" ),
      ( "WGT", "Weight", "" ),
      ( "BDATE", "Birth Date", "" ),

      #Biomarker
      ( "BMX", "Biomarker X", "" ),
      ( "BMY", "Biomarker Y", "" )
    ]
    study_data_items = []
    for data in raw_study_data:
      study_data_items.append(study_data_data(*data))
    #print(study_data_items)

    # Activities
    # Short Name, Description, Procedures, Study Data
    study_activity_data = [
      ("Informed Consent", "Informed consent is obtained at screening", [], []),
      ("Eligibility Screening", "Inclusion and Exclusion criteria evaluation", [], []),
      ("Hematology", "Hematology assessment in blood samples", [], study_data_items[0:3]),
      ("Biochemistry", "Biochemistry assessment in plasma samples", [], study_data_items[3:3]),
      ("Demographics", "Demographics", [], study_data_items[6:3]),
      ("Dosing", "Dosing of Drug A - 2 times a week", [], []),
      ("Plasma Biomarker", "Biomarker assessments for xxx", [], study_data_items[9:2]),
      ("PK", "PK Sample", [], [])
    ]
    #print(study_activity_data[2])
    activities = []
    for activity in study_activity_data:
      activities.append(activity_data(*activity))
    double_link(activities, 'previousActivityId', 'nextActivityId')

    # Visits
    a_visit = code_for('Encounter', 'encounterType', submission_value='Visit')   
    clinic_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')   
    hospital_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C16696')   
    in_person_mode = code_for('Encounter', 'encounterContactMode', c_code='C175574')    
    remote_audio_mode = code_for('Encounter', 'encounterContactMode', c_code='C171525')    

    # name, description, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None
    study_encounter_data = [
      ("Screening", "SCREENING", a_visit, clinic_setting, in_person_mode, rules[0], rules[18]),
      ("Day 1", "DAY 1", a_visit, hospital_setting, in_person_mode, rules[1], None),
      ("Week 1", "WEEK 1", a_visit, hospital_setting, in_person_mode, rules[2], rules[19]),
      ("Week 2", "WEEK 2", a_visit, hospital_setting, in_person_mode, rules[3], rules[20]),
      ("Week 3", "WEEK 3", a_visit, hospital_setting, in_person_mode, rules[4], rules[21]),
      ("Week 4", "WEEK 4", a_visit, hospital_setting, in_person_mode, rules[5], rules[22]),
      ("Week 5", "WEEK 5", a_visit, hospital_setting, in_person_mode, rules[6], rules[23]),
      ("Week 6", "WEEK 6", a_visit, hospital_setting, in_person_mode, rules[7], rules[24]),
      ("Week 7", "WEEK 7", a_visit, hospital_setting, in_person_mode, rules[8], rules[25]),
      ("Week 8", "WEEK 8", a_visit, hospital_setting, in_person_mode, rules[9], rules[26]),
      ("Week 9", "WEEK 9", a_visit, hospital_setting, in_person_mode, rules[10], rules[27]),
      ("Week 10", "WEEK 10", a_visit, hospital_setting, in_person_mode, rules[11], rules[28]),
      ("Week 11", "WEEK 11", a_visit, hospital_setting, in_person_mode, rules[12], rules[29]),
      ("Week 12", "WEEK 12", a_visit, hospital_setting, in_person_mode, rules[13], rules[30]),
      ("Week 13", "WEEK 13", a_visit, hospital_setting, in_person_mode, rules[14], rules[31]),
      ("Week 14", "WEEK 14", a_visit, hospital_setting, in_person_mode, rules[15], rules[32]),
      ("Week 15", "WEEK 15", a_visit, hospital_setting, in_person_mode, rules[16], rules[33]),
      ("Week 16", "WEEK 16", a_visit, hospital_setting, in_person_mode, rules[17], rules[34]),
      ("Follow up", "FOLLOW-UP",	a_visit, hospital_setting, in_person_mode, None, None)
    ]

    encounters = []
    for encounter in study_encounter_data:
      encounters.append(encounter_data(*encounter))
    double_link(encounters, 'previousEncounterId', 'nextEncounterId')

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

    # Investigational Interventions
    ii_code_1 = code_data( "XX031ZA", "ATC", "2021", "SubstX")
    ii_1 = investigational_intervention_data("Treatment with substX", [ii_code_1])
    ii = [ii_1]
						
    # Study Populations
    study_population_1 = study_design_population_data("A metastatic cancer population")

    # Endpoints
    primary_endpoint = code_for('Endpoint', 'endpointLevel', submission_value='Primary Endpoint')
    endpoint_1 = endpoint_data(
      "Survival rate after cycle 8 of treatment",
      "EFFICACY",
      primary_endpoint
    )

    # Objectives
    primary_objective = code_for('Objective', 'objectiveLevel', submission_value='Study Primary Objective')
    objective_1 = objective_data(
      "Evaluate sensitivity index from baseline to end of study (16 weeks)", 
      primary_objective, 
      [endpoint_1]
    )
    objectives = [objective_1]

    # Indications
    code_1 = code_data( "E11", "ICD-10-CM", "10", "Type 2 diabetes mellitus")
    code_2 = code_data( "44054006", "SNOMED", "2022", "Diabetes mellitus type 2 (disorder)"	)
    code_3 = code_data( "E10", "ICD-10-CM", "10", "Type 1 diabetes mellitus")
    code_4 = code_data( "44635009", "SNOMED", "2022", "Diabetes mellitus type 1 (disorder)"	)

    indication_1 = study_indication_data("Diabetes Type II", [code_1, code_2])
    indication_2 = study_indication_data("Diabetes Type I", [code_3, code_4])
    indications = [indication_1, indication_2]

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

    # Analysis Populations
    analysis_population_1 = analysis_population_data("ITT")
    analysis_population_2 = analysis_population_data("PP")

    # Estimands
    estimand_1 = estimand_data("Measure 1", analysis_population_1, ii_1, endpoint_1, [i_event_1])
    estimand_2 = estimand_data("Measure 2", analysis_population_2, ii_1, endpoint_1, [i_event_2, i_event_3, i_event_4])
    estimands = [estimand_1, estimand_2]

    # Study Arms
    origin_type = code_for('StudyArm', 'studyArmDataOriginType', submission_value='Data Generated Within Study') 
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    study_arm_1 = study_arm_data("Treatment", "Treatment", treatment, "Captured subject data", origin_type)

    # Epochs
    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    screening = code_for('StudyEpoch', 'studyEpochType', submission_value='SCREENING') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    
    # name, description, epoch_type, encounters
    raw_epoch_data = [
      ("Screening", "Screening", screening, [encounters[0]]),
      ("Titration Period 1", "Titration Period 1", treatment, [ encounters[1], encounters[2], encounters[3], encounters[4], encounters[5] ]),
      ("Titration Period 2", "Titration Period 2", treatment, [ encounters[6], encounters[7], encounters[8], encounters[9] ]),
      ("Titration Period 3", "Titration Period 3", treatment, [ encounters[10], encounters[11], encounters[12], encounters[13] ]),
      ("Titration Period 4", "Titration Period 4", treatment, [ encounters[14], encounters[15], encounters[16], encounters[17] ]),
      ("Follow-upP", "Follow-up", follow_up, [ encounters[18] ])
    ]
    epochs = []
    for epoch in raw_epoch_data:
      epochs.append(study_epoch_data(*epoch))
    double_link(epochs, 'previousStudyEpochId', 'nextStudyEpochId')
    #print(epochs)

    # Elements
    # name, description, start rule, end rule
    raw_element_data = [
      ("Screening", "Screening", rules[35], rules[40]),
      ("Titration Period 1", "dose range 10 mg to 20 mg", rules[36], rules[41]),
      ("Titration Period 2", "dose range 20 mg to 30 mg", rules[37], rules[42]),
      ("Titration Period 3", "dose range 30 mg to 40 mg", rules[38], rules[43]),
      ("Titration Period 4", "dose range 40 mg to 50 mg", rules[39], rules[44]),
      ("FOLLOW_UP", "Follow up", None, None),
    ]
    elements = []
    for element in raw_element_data:
      elements.append(study_element_data(*element))

    study_cells = []
    study_cells.append(study_cell_data(study_arm_1, epochs[0], [ elements[0] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[1], [ elements[1] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[2], [ elements[2] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[3], [ elements[3] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[4], [ elements[4] ]))
    study_cells.append(study_cell_data(study_arm_1, epochs[5], [ elements[5] ]))

    intent = code_for('StudyDesign', 'trialIntentType', submission_value='CURE')
    design_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='SEQUENTIAL')

    design_1 = study_design_data([intent], design_type, int_model, study_cells, indications, objectives, [study_population_1], ii, [workflow], estimands)
    designs = [design_1]

    # Protocol versions
    # brief_title, official_title, public_title, scientific_title, version, amendment, effective_date, status):
    draft_status = code_for('StudyProtocolVersion', 'protocolStatus', submission_value='Draft')
    protocol_version_1 = study_protocol_version_data(
      "BMS", 
      "BMS Study Official title", 
      "BMS Study Public title",
      "BMS Study Scientific title",
      "1", 
      None, 
      "2022-01-01", 
      draft_status
    )
    protocol_versions = [protocol_version_1]

    # Study Identifiers
    registry_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Registry')
    sponsor_type = code_for('Organization', 'organizationType', submission_value='Clinical Study Sponsor')
    regulator_type = code_for('Organization', 'organizationType', submission_value='Regulatory Agency')
    organisation_1 = organization_data("DUNS", "123456789", "ACME Pharma", sponsor_type)
    organisation_2 = organization_data("USGOV", "CT-GOV", "ClinicalTrials.gov", registry_type)
    organisation_3 = organization_data("FDA", "FDA", "Food and Drug Adminstration", regulator_type)
    organisation_4 = organization_data("EMA", "EMA", "European Medicines Agency", regulator_type)
    identifier_1 = study_identifier_data("XX03CC05", organisation_1)
    identifier_2 = study_identifier_data("NCT12345678", organisation_2)
    identifier_3 = study_identifier_data("FDA1234", organisation_3)
    identifier_4 = study_identifier_data("EMA1234", organisation_4)
    identifiers = [identifier_1, identifier_2, identifier_3, identifier_4]

    # Assemble complete study
    study_title = "BMS Test Study"
    phase = code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase II Trial")
    study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
    return study_data(study_title, "1", study_type, phase, identifiers, protocol_versions, designs)

