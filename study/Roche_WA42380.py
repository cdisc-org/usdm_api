from factory.factory import *

class RocheWA42380():

  def json():

    # Rules
    study_rule_data = [
      # Element Start Rules
      ("Informed consent", "Rule 1"),
      ("First dose of a treatment epoch, where the does is XXX", "Rule 2"),
      ("First dose of a treatment epoch, where the does is placebo", "Rule 3"),
      ("28 days after first dose of the previous treatment epoch", "Rule 4"),

      # Element End Rules
      ("As soon as possibe once screening is complete", "Rule 5"),
      ("After 28 days, where the does is XXX", "Rule 6"),
      ("After 28 days, where the does is XXX", "Rule 7"),
      ("After day 60", "Rule 8"),

      # Visit Start Rules
      ("Start of screening epoch", "Rule 8"),
      ("4 hours pprior to end of screening epoch", "Rule 9"),
      ("15 minutes after the end of basline epoch", "Rule 10"),

      ("24 hours after the start of the treatment epoch", "Rule 11"),
      ("3 days after the start of the treatment epoch", "Rule 12"),
      ("4 days after the start of the treatment epoch", "Rule 13"),
      ("5 days after the start of the treatment epoch", "Rule 14"),
      ("6 days after the start of the treatment epoch", "Rule 15"),
      ("7 days after the start of the treatment epoch", "Rule 16"),
      ("8 days after the start of the treatment epoch", "Rule 17"),
      ("9 days after the start of the treatment epoch", "Rule 18"),
      ("10 days after the start of the treatment epoch", "Rule 19"),
      ("11 days after the start of the treatment epoch", "Rule 20"),
 
      ("12 days after the start of the treatment epoch", "Rule 21"),
      ("13 days after the start of the treatment epoch", "Rule 22"),
      ("14 days after the start of the treatment epoch", "Rule 23"),
      ("15 days after the start of the treatment epoch", "Rule 24"),
      ("16 days after the start of the treatment epoch", "Rule 25"),
      ("17 days after the start of the treatment epoch", "Rule 26"),
      ("18 days after the start of the treatment epoch", "Rule 27"),
      ("19 days after the start of the treatment epoch", "Rule 28"),
      ("20 days after the start of the treatment epoch", "Rule 29"),
      ("21 days after the start of the treatment epoch", "Rule 30"),
   
      ("22 days after the start of the treatment epoch", "Rule 31"),
      ("23 days after the start of the treatment epoch", "Rule 32"),
      ("24 days after the start of the treatment epoch", "Rule 33"),
      ("25 days after the start of the treatment epoch", "Rule 34"),
      ("26 days after the start of the treatment epoch", "Rule 35"),
      ("27 days after the start of the treatment epoch", "Rule 36"),
      ("28 days after the start of the treatment epoch", "Rule 37"),
      ("35 days (+/- 3 days) after the start of the treatment epoch", "Rule 38"),
      ("45 days (+/- 3 days) after the start of the treatment epoch", "Rule 39"),
      ("60 days (+/- 3 days) after the start of the treatment epoch", "Rule 40"),

      # Visit End Rules

      ("Start of treatment epoch", "Rule 41"),
      # No visit 2 end rule
      # No visit 2 end rule
      # Days 3 to 28 no end rule
      # Days 35, 45 no end rule
      ("At visit completion (trial exit)", "Rule 42"),
    ]

    rules = []
    for rule in study_rule_data:
      rules.append(transition_rule_data(rule[0], rule[1]))

    # <<<<< To be added >>>>>
    # Procedures

    # <<<<< More to be added >>>>>
    # Study Data
    raw_study_data = [
      # Demographics
      ( "Age", "Age", ""),
      ( "Sex", "Sex", ""),
      ( "Race", "Race", ""),

      # Physical Examination (3)
      ( "Head", "", ""),
      ( "Eyes", "", ""),
      ( "Ears", "", ""),
      ( "Nose", "", ""),
      ( "Throat", "", ""),
      ( "Cardiovascular", "", ""),
      ( "Dermatologi", "", ""),
      ( "Musculoskeletal", "", ""),
      ( "Respiratory", "", ""),
      ( "Gastrointestinal", "", ""),
      ( "Genitourinary", "", ""),
      ( "Neurologic", "", ""),

      # Chemistry (15)
      ( "Bicarbonate", "bicarbonate", "" ),
      ( "Total carbon dioxide", "total carbon dioxide", "" ),
      ( "Sodium", "sodium", "" ),
      ( "Potassium", "potassium", "" ),
      ( "Chloride", "chloride", "" ),
      ( "Glucose", "glucose", "" ),
      ( "Blood urea nitrogen", "Blood urea nitrogen", "" ),
      ( "Urea", "Urea", "" ),
      ( "Creatinine", "creatinine", "" ),
      ( "Total protein", "total protein", "" ),
      ( "Albumin", "albumin", "" ),
      ( "Phosphorus", "Phosphorus", "" ),
      ( "Calcium", "Calcium", "" ),
      ( "Total bilirubin", "Total bilirubin", "" ),
      ( "ALP", "Alkaline Phosphatase", "" ),
      ( "ALT", "Alanine Transaminase", "" ),
      ( "AST", "Aspartate Aminotransferase", "" ),
      ( "Uric acid", "uric acid", "" ),
      ( "LDH", "Lactate Dehydrogenase", "" ),
      ( "Ferritin", "ferritin", "" ),
      ( "D-dimer", "D-dimer", "" ),

      # Hematology (35)
      ( "RBC", "Red Blood Cell count", "" ),
      ( "HCT", "Hematocrit", "" ),
      ( "WBC", "White blood Cell count", "" ),
      ( "Hemoglobin", "Hemoglobin", ""),
      ( "platelet count", "platelet count", ""),
      ( "", "differential count (neutrophils, eosinophils, basophils, monocytes, lymphocytes)", ""),
      ( "", "lymphocyte subsets (T cells, B cells, and NK cells)", ""),

      # Vital Signs (42)
      ( "Respiratory rate", "respiratory rate", ""),
      ( "Pulse rate", "pulse rate", ""),
      ( "Systolic blood pressure", "sysolic blodd pressure", ""),
      ( "Diastolic blood pressures", "diastolic blood pressures", ""),
      ( "Body temperature, ", "body temperature", ""),
      ( "Oxygen saturation", "oxygen saturation", ""),
      ( "NEWS2", "National Early Warning Score 2", ""),
      
      # Weight (49) 
      ( "Weight", "Weight", "" ),

    ]
    study_data_items = []
    for data in raw_study_data:
      # print(*data)
      study_data_items.append(study_indication_data(*data))

    # Activities
    # Short Name, Description, Procedures, Study Data
    study_activity_data = [
      ("Informed consent", "Informed consent", [], []),
      ("Inclusion/exclusion criteria", "Inclusion/exclusion criteria", [], []),
      ("Demographics", "Demographic data", [], study_data_items[0:3]),
      ("Randomization", "Randomization", [], []),
      ("Medical history", "Medical history", [], []),
      ("Physical examination", "Complete physical examination", [], study_data_items[3:15]),
      ("Weight", "Weight", [], study_data_items[49:50]),
      ("COVID-19 diagnosis", "COVID-19 diagnosis", [], []),
      ("Chest X-ray/CT scan", "Chest X-ray/CT scan", [], []),
      ("ECG", "Electrocardiogram", [], []),
      ("Pregnancy test", "Pregnancy test", [], []),
      # 11
      ("PaO2/FiO2", "arterial oxygen partial pressure/fraction of inspired oxygen", [], []),
      ("SpO2", "peripheral capillary oxygen saturation", [], []),
      ("Vital signs", "Vital signs", [], study_data_items[42:49]),
      ("Ordinal scoring", "Ordinal scoring", [], []),
      ("Adverse events", "Adverse events", [], []),
      ("Concomitant medications", "Concomitant medications", [], []),
      ("Hematology", "Hematology", [], study_data_items[35:42]),
      ("Chemistry", "Chemistry", [], study_data_items[15:35]),
      ("Study drug administration", "Study drug administration", [], []),
      ("Central Labs", "Central Labs", [], []),
      # 21
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
    double_link(activities, 'activityId', 'previousActivityId', 'nextActivityId')

    # Visits
    # Codes
    a_visit = code_for('Encounter', 'encounterType', submission_value='Visit')   
    clinic_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C51282')   
    hospital_setting = code_for('Encounter', 'encounterEnvironmentalSetting', c_code='C16696')   
    in_person_mode = code_for('Encounter', 'encounterContactModes', c_code='C175574')    
    remote_audio_mode = code_for('Encounter', 'encounterContactModes', c_code='C171525')    
    # Fields: name, description, encounter_type, env_setting, contact_mode, start_rule=None, end_rule=None
    study_encounter_data = [
      ("encounter_1", "Screening", "SCREENING", a_visit, clinic_setting, in_person_mode),
      ("encounter_2", "Baseline", "BASELINE", a_visit, hospital_setting, in_person_mode),
      ("encounter_3", "Day 1", "Day 1", a_visit, hospital_setting, in_person_mode),
      ("encounter_4", "Day 2A", "Day 2A", a_visit, hospital_setting, in_person_mode),
      ("encounter_5", "Day 2B", "Day 2B", a_visit, hospital_setting, in_person_mode),
      ("encounter_6", "Day 3", "Day 3", a_visit, hospital_setting, in_person_mode),
      ("encounter_7", "Day 4", "Day 4", a_visit, hospital_setting, in_person_mode),
      ("encounter_8", "Day 5", "Day 5", a_visit, hospital_setting, in_person_mode),
      ("encounter_9", "Day 6", "Day 6", a_visit, hospital_setting, in_person_mode),
      ("encounter_10", "Day 7", "Day 7", a_visit, hospital_setting, in_person_mode),
      ("encounter_11", "Day 8", "Day 8", a_visit, hospital_setting, in_person_mode),
      # 11
      ("encounter_12", "Day 9", "Day 9", a_visit, hospital_setting, in_person_mode),
      ("encounter_13", "Day 10", "Day 10", a_visit, hospital_setting, in_person_mode),
      ("encounter_14", "Day 11", "Day 11", a_visit, hospital_setting, in_person_mode),
      ("encounter_15", "Day 12", "Day 12", a_visit, hospital_setting, in_person_mode),
      ("encounter_16", "Day 13", "Day 13", a_visit, hospital_setting, in_person_mode),
      ("encounter_17", "Day 14", "Day 14", a_visit, hospital_setting, in_person_mode),
      ("encounter_18", "Day 15", "Day 15", a_visit, hospital_setting, in_person_mode),
      ("encounter_19", "Day 16", "Day 16", a_visit, hospital_setting, in_person_mode),
      ("encounter_20", "Day 17", "Day 17", a_visit, hospital_setting, in_person_mode),
      ("encounter_21", "Day 18", "Day 18", a_visit, hospital_setting, in_person_mode),
      # 21
      ("encounter_22", "Day 19", "Day 19", a_visit, hospital_setting, in_person_mode),
      ("encounter_23", "Day 20", "Day 20", a_visit, hospital_setting, in_person_mode),
      ("encounter_24", "Day 21", "Day 21", a_visit, hospital_setting, in_person_mode),
      ("encounter_25", "Day 22", "Day 22", a_visit, hospital_setting, in_person_mode),
      ("encounter_26", "Day 23", "Day 23", a_visit, hospital_setting, in_person_mode),
      ("encounter_27", "Day 24", "Day 24", a_visit, hospital_setting, in_person_mode),
      ("encounter_28", "Day 25", "Day 25", a_visit, hospital_setting, in_person_mode),
      ("encounter_29", "Day 26", "Day 26", a_visit, hospital_setting, in_person_mode),
      ("encounter_30", "Day 27", "Day 27", a_visit, hospital_setting, in_person_mode),
      ("encounter_31", "Day 28", "Day 28", a_visit, hospital_setting, in_person_mode),
      # 31
      ("encounter_32", "Day 35", "Day 35", a_visit, hospital_setting, in_person_mode),
      ("encounter_33", "Day 45", "Day 45", a_visit, hospital_setting, in_person_mode),
      ("encounter_34", "Day 60", "Day 60", a_visit, hospital_setting, in_person_mode),
    ]

    encounters = []
    for encounter in study_encounter_data:
      encounters.append(encounter_data(*encounter))
    double_link(encounters, 'encounterId', 'previousEncounterId', 'nextEncounterId')
    
    # <<<<< Need setting up >>>>>
    # Work Flow Items
    wfi_links = [
      [ encounters[0], activities[0] ], 
      [ encounters[0], activities[1] ], 
      [ encounters[0], activities[2] ], 
      [ encounters[0], activities[5] ], 
      [ encounters[0], activities[7] ], 
      [ encounters[0], activities[8] ], 
      [ encounters[0], activities[9] ], 
      [ encounters[0], activities[10] ], 
      [ encounters[0], activities[11] ], 
      [ encounters[0], activities[12] ], 
      [ encounters[0], activities[13] ], 
      [ encounters[0], activities[17] ], 
      [ encounters[0], activities[18] ], 

      [ encounters[1], activities[1] ], 
      [ encounters[1], activities[3] ], 
      [ encounters[1], activities[4] ], 
      [ encounters[1], activities[6] ], 
      [ encounters[1], activities[12] ], 
      [ encounters[1], activities[13] ], 
      [ encounters[1], activities[14] ], 
      [ encounters[1], activities[15] ], 
      [ encounters[1], activities[16] ], 
      [ encounters[1], activities[17] ], 
      [ encounters[1], activities[18] ], 
      [ encounters[1], activities[19] ], 
      [ encounters[1], activities[20] ], 
      [ encounters[1], activities[21] ], 
      [ encounters[1], activities[22] ], 
      [ encounters[1], activities[23] ], 
      [ encounters[1], activities[24] ], 
      [ encounters[1], activities[25] ], 
      [ encounters[1], activities[26] ], 
      [ encounters[1], activities[27] ], 

      [ encounters[2], activities[12] ], 
      [ encounters[2], activities[13] ], 
      [ encounters[2], activities[21] ], 
      [ encounters[2], activities[22] ], 

      [ encounters[3], activities[12] ], 
      [ encounters[3], activities[13] ], 
      [ encounters[3], activities[14] ], 
      [ encounters[3], activities[15] ], 
      [ encounters[3], activities[16] ], 
      [ encounters[3], activities[17] ], 
      [ encounters[3], activities[18] ], 
      [ encounters[3], activities[19] ], 
      [ encounters[3], activities[21] ], 
      [ encounters[3], activities[22] ], 
      [ encounters[3], activities[23] ], 
      [ encounters[3], activities[24] ], 
      [ encounters[3], activities[26] ], 

      [ encounters[4], activities[12] ], 
      [ encounters[4], activities[13] ], 
      [ encounters[4], activities[21] ], 
      [ encounters[4], activities[22] ], 

      [ encounters[5], activities[13] ], 
      [ encounters[5], activities[11] ], 
      [ encounters[5], activities[12] ], 
      [ encounters[5], activities[14] ], 
      [ encounters[5], activities[15] ], 
      [ encounters[5], activities[16] ], 
      [ encounters[5], activities[17] ], 
      [ encounters[5], activities[18] ], 
      [ encounters[5], activities[21] ], 
      [ encounters[5], activities[23] ], 
      [ encounters[5], activities[24] ], 
      [ encounters[5], activities[26] ], 
      [ encounters[5], activities[27] ], 

      [ encounters[6], activities[13] ], 
      [ encounters[6], activities[11] ], 
      [ encounters[6], activities[12] ], 
      [ encounters[6], activities[14] ], 
      [ encounters[6], activities[15] ], 
      [ encounters[6], activities[16] ], 
      [ encounters[6], activities[24] ], 

      [ encounters[7], activities[13] ], 
      [ encounters[7], activities[11] ], 
      [ encounters[7], activities[12] ], 
      [ encounters[7], activities[14] ], 
      [ encounters[7], activities[15] ], 
      [ encounters[7], activities[16] ], 
      [ encounters[7], activities[24] ], 

      [ encounters[8], activities[13] ], 
      [ encounters[8], activities[11] ], 
      [ encounters[8], activities[12] ], 
      [ encounters[8], activities[14] ], 
      [ encounters[8], activities[15] ], 
      [ encounters[8], activities[16] ], 
      [ encounters[8], activities[24] ], 

      [ encounters[9], activities[8] ], 
      [ encounters[9], activities[13] ], 
      [ encounters[9], activities[11] ], 
      [ encounters[9], activities[12] ], 
      [ encounters[9], activities[14] ], 
      [ encounters[9], activities[15] ], 
      [ encounters[9], activities[16] ], 
      [ encounters[9], activities[17] ], 
      [ encounters[9], activities[18] ], 
      [ encounters[9], activities[21] ], 
      [ encounters[9], activities[22] ], 
      [ encounters[9], activities[23] ], 
      [ encounters[9], activities[24] ], 
      [ encounters[9], activities[26] ], 
      [ encounters[9], activities[27] ], 

      [ encounters[10], activities[13] ], 
      [ encounters[10], activities[11] ], 
      [ encounters[10], activities[12] ], 
      [ encounters[10], activities[14] ], 
      [ encounters[10], activities[15] ], 
      [ encounters[10], activities[16] ], 

      [ encounters[11], activities[13] ], 
      [ encounters[11], activities[11] ], 
      [ encounters[11], activities[12] ], 
      [ encounters[11], activities[14] ], 
      [ encounters[11], activities[15] ], 
      [ encounters[11], activities[16] ], 

      [ encounters[12], activities[13] ], 
      [ encounters[12], activities[11] ], 
      [ encounters[12], activities[12] ], 
      [ encounters[12], activities[14] ], 
      [ encounters[12], activities[15] ], 
      [ encounters[12], activities[16] ], 
      [ encounters[12], activities[17] ], 
      [ encounters[12], activities[18] ], 
      [ encounters[12], activities[24] ], 

      [ encounters[13], activities[13] ], 
      [ encounters[13], activities[11] ], 
      [ encounters[13], activities[12] ], 
      [ encounters[13], activities[14] ], 
      [ encounters[13], activities[15] ], 
      [ encounters[13], activities[16] ], 

      [ encounters[14], activities[13] ], 
      [ encounters[14], activities[11] ], 
      [ encounters[14], activities[12] ], 
      [ encounters[14], activities[14] ], 
      [ encounters[14], activities[15] ], 
      [ encounters[14], activities[16] ], 

      [ encounters[15], activities[13] ], 
      [ encounters[15], activities[11] ], 
      [ encounters[15], activities[12] ], 
      [ encounters[15], activities[14] ], 
      [ encounters[15], activities[15] ], 
      [ encounters[15], activities[16] ], 

      [ encounters[16], activities[8] ], 
      [ encounters[16], activities[13] ], 
      [ encounters[16], activities[11] ], 
      [ encounters[16], activities[12] ], 
      [ encounters[16], activities[14] ], 
      [ encounters[16], activities[15] ], 
      [ encounters[16], activities[16] ], 
      [ encounters[16], activities[17] ], 
      [ encounters[16], activities[18] ], 
      [ encounters[16], activities[21] ], 
      [ encounters[16], activities[22] ], 
      [ encounters[16], activities[23] ], 
      [ encounters[16], activities[24] ], 
      [ encounters[16], activities[26] ], 

      [ encounters[17], activities[13] ], 
      [ encounters[17], activities[11] ], 
      [ encounters[17], activities[12] ], 
      [ encounters[17], activities[14] ], 
      [ encounters[17], activities[15] ], 
      [ encounters[17], activities[16] ], 

      [ encounters[18], activities[13] ], 
      [ encounters[18], activities[11] ], 
      [ encounters[18], activities[12] ], 
      [ encounters[18], activities[14] ], 
      [ encounters[18], activities[15] ], 
      [ encounters[18], activities[16] ], 

      [ encounters[19], activities[13] ], 
      [ encounters[19], activities[11] ], 
      [ encounters[19], activities[12] ], 
      [ encounters[19], activities[14] ], 
      [ encounters[19], activities[15] ], 
      [ encounters[19], activities[16] ], 

      [ encounters[20], activities[13] ], 
      [ encounters[20], activities[11] ], 
      [ encounters[20], activities[12] ], 
      [ encounters[20], activities[14] ], 
      [ encounters[20], activities[15] ], 
      [ encounters[20], activities[16] ], 

      [ encounters[21], activities[13] ], 
      [ encounters[21], activities[11] ], 
      [ encounters[21], activities[12] ], 
      [ encounters[21], activities[14] ], 
      [ encounters[21], activities[15] ], 
      [ encounters[21], activities[16] ], 

      [ encounters[22], activities[13] ], 
      [ encounters[22], activities[11] ], 
      [ encounters[22], activities[12] ], 
      [ encounters[22], activities[14] ], 
      [ encounters[22], activities[15] ], 
      [ encounters[22], activities[16] ], 

      [ encounters[23], activities[8] ], 
      [ encounters[23], activities[13] ], 
      [ encounters[23], activities[11] ], 
      [ encounters[23], activities[12] ], 
      [ encounters[23], activities[14] ], 
      [ encounters[23], activities[15] ], 
      [ encounters[23], activities[16] ], 
      [ encounters[23], activities[17] ], 
      [ encounters[23], activities[18] ], 
      [ encounters[23], activities[21] ], 
      [ encounters[23], activities[22] ], 
      [ encounters[23], activities[23] ], 
      [ encounters[23], activities[24] ], 
      [ encounters[23], activities[26] ], 

      [ encounters[24], activities[13] ], 
      [ encounters[24], activities[11] ], 
      [ encounters[24], activities[12] ], 
      [ encounters[24], activities[14] ], 
      [ encounters[24], activities[15] ], 
      [ encounters[24], activities[16] ], 

      [ encounters[25], activities[13] ], 
      [ encounters[25], activities[11] ], 
      [ encounters[25], activities[12] ], 
      [ encounters[25], activities[14] ], 
      [ encounters[25], activities[15] ], 
      [ encounters[25], activities[16] ], 

      [ encounters[26], activities[13] ], 
      [ encounters[26], activities[11] ], 
      [ encounters[26], activities[12] ], 
      [ encounters[26], activities[14] ], 
      [ encounters[26], activities[15] ], 
      [ encounters[26], activities[16] ], 

      [ encounters[27], activities[13] ], 
      [ encounters[27], activities[11] ], 
      [ encounters[27], activities[12] ], 
      [ encounters[27], activities[14] ], 
      [ encounters[27], activities[15] ], 
      [ encounters[27], activities[16] ], 

      [ encounters[28], activities[13] ], 
      [ encounters[28], activities[11] ], 
      [ encounters[28], activities[12] ], 
      [ encounters[28], activities[14] ], 
      [ encounters[28], activities[15] ], 
      [ encounters[28], activities[16] ], 

      [ encounters[29], activities[13] ], 
      [ encounters[29], activities[11] ], 
      [ encounters[29], activities[12] ], 
      [ encounters[29], activities[14] ], 
      [ encounters[29], activities[15] ], 
      [ encounters[29], activities[16] ], 

      [ encounters[30], activities[8] ], 
      [ encounters[30], activities[13] ], 
      [ encounters[30], activities[11] ], 
      [ encounters[30], activities[12] ], 
      [ encounters[30], activities[14] ], 
      [ encounters[30], activities[15] ], 
      [ encounters[30], activities[16] ], 
      [ encounters[30], activities[17] ], 
      [ encounters[30], activities[18] ], 
      [ encounters[30], activities[21] ], 
      [ encounters[30], activities[22] ], 
      [ encounters[30], activities[23] ], 
      [ encounters[30], activities[24] ], 
      [ encounters[30], activities[26] ], 
      [ encounters[30], activities[27] ], 

      [ encounters[31], activities[24] ], 
      [ encounters[31], activities[13] ], 
      [ encounters[31], activities[12] ], 
      [ encounters[31], activities[14] ], 
      [ encounters[31], activities[15] ], 
      [ encounters[31], activities[16] ], 
      [ encounters[31], activities[17] ], 
      [ encounters[31], activities[18] ], 
      [ encounters[31], activities[21] ], 
      [ encounters[31], activities[22] ], 
      [ encounters[31], activities[23] ], 

      [ encounters[32], activities[24] ], 
      [ encounters[32], activities[13] ], 
      [ encounters[32], activities[12] ], 
      [ encounters[32], activities[14] ], 
      [ encounters[32], activities[15] ], 
      [ encounters[32], activities[16] ], 
      [ encounters[32], activities[17] ], 
      [ encounters[32], activities[18] ], 

      [ encounters[33], activities[8] ], 
      [ encounters[33], activities[24] ], 
      [ encounters[33], activities[13] ], 
      [ encounters[33], activities[12] ], 
      [ encounters[33], activities[14] ], 
      [ encounters[33], activities[15] ], 
      [ encounters[33], activities[16] ], 
      [ encounters[33], activities[17] ], 
      [ encounters[33], activities[18] ], 
      [ encounters[33], activities[21] ], 
      [ encounters[33], activities[22] ], 
      [ encounters[33], activities[23] ], 
      [ encounters[33], activities[25] ]

    ]
    wfis = []
    workflow_count = 0
    for item in wfi_links:
      workflow_count = workflow_count + 1
      id = 'workflowItem%s' % workflow_count
      desc = 'Workflow Item %s' % workflow_count
      wfis.append(workflow_item_data(id, desc, encounter=item[0]["encounterId"], activity=item[1]["activityId"]))
    workflow = workflow_data("workflow1", "Workflow 1", wfis)
    double_link(wfis, 'workflowItemId', 'previousWorkflowItemId', 'nextWorkflowItemId')  

    # <<<<< Need setting up >>>>>
    # Investigational Interventions
    ii_code_1 = code_data( "XX031ZA", "ATC", "2021", "SubstX")
    ii_1 = investigational_intervention_data("ii_1", "Treatment with substX", [ii_code_1])
    ii = [ii_1]
						
    # <<<<< Need setting up >>>>>
    # Study Populations
    study_population_1 = study_design_population_data("study_population_1", "A metastatic cancer population")

    # <<<<< Need setting up >>>>>
    # Endpoints
    primary_endpoint = code_for('Endpoint', 'endpointLevel', submission_value='Primary Endpoint')
    endpoint_1 = endpoint_data(
      "endpoint_1",
      "Survival rate after cycle 8 of treatment",
      "EFFICACY",
      primary_endpoint
    )

    # <<<<< Need setting up >>>>>
    # Objectives
    primary_objective = code_for('Objective', 'objectiveLevel', submission_value='Study Primary Objective')
    objective_1 = objective_data(
      "objective_1",
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
    indication_1 = study_indication_data("indication_1", "Diabetes Type II", [code_1, code_2])
    indication_2 = study_indication_data("indication_2", "Diabetes Type I", [code_3, code_4])
    indications = [indication_1, indication_2]

    # <<<<< Need setting up >>>>>
    # Intercurrent Events
    i_event_1 = intercurrent_event_data(
      "i_event_1",
      "Termination", 
      "Termination",
      "Patients with out of range lab values before dosing will be excluded"
    )
    i_event_2 = intercurrent_event_data(
      "i_event_2",
      "Missed dose",
      "Missed dose",
      "Patients with 1 missed dose will be included. Patients with >1 missed dose will be excluded"
    )
    i_event_3 = intercurrent_event_data(
      "i_event_3",
      "Termination",
      "Termination",
      "Patients with out of range lab values before dosing will be excluded"
    )
    i_event_4 = intercurrent_event_data(
      "i_event_4",
      "Out of range lab values",
      "Out of range lab values",
      "Patients with out of range lab values before dosing will be excluded"
    )

    # <<<<< Need setting up >>>>>
    # Analysis Populations
    analysis_population_1 = analysis_population_data("analysis_population_1", "ITT")
    analysis_population_2 = analysis_population_data("analysis_population_2", "PP")

    # <<<<< Need setting up >>>>>
    # Estimands
    estimand_1 = estimand_data("estimand_1", "Measure 1", analysis_population_1, "Treatment with substX", "Blood Pressure", [i_event_1])
    estimand_2 = estimand_data("estimand_2", "Measure 2", analysis_population_2, "Treatment with substX", "Blood Pressure", [i_event_2, i_event_3, i_event_4])
    estimands = [estimand_1, estimand_2]

    # Study Arms
    # Codes
    origin_type = code_for('StudyArm', 'studyArmDataOriginType', submission_value='Data Generated Within Study') 
    treatment = code_for('StudyArm', 'studyArmType', submission_value='Treatment Arm')
    placebo = code_for('StudyArm', 'studyArmType', submission_value='Placebo Comparator Arm')
    # Fields: name, description, arm_type, origin_description, origin_type
    study_arm_1 = study_arm_data("study_arm_1", "TCZ+SOC", "Tocilizumab with SOC", treatment, "Captured subject data", origin_type)
    study_arm_2 = study_arm_data("study_arm_2", "Placebo+SOC", "Palcebo with SOC", placebo, "Captured subject data", origin_type)

    # <<<<< Links to encounters need setting up >>>>>
    # Epochs
    # Codes
    run_in = code_for('StudyEpoch', 'studyEpochType', submission_value='RUN-IN') 
    screening = code_for('StudyEpoch', 'studyEpochType', submission_value='SCREENING') 
    treatment = code_for('StudyEpoch', 'studyEpochType', submission_value='TREATMENT')
    follow_up = code_for('StudyEpoch', 'studyEpochType', submission_value='FOLLOW-UP')
    encounter_ids_2 = [encounter['encounterId'] for encounter in encounters[1:31]]
    encounter_ids_3 = [encounter['encounterId'] for encounter in encounters[31:34]]
    # Fields: name, description, epoch_type, encounters
    raw_epoch_data = [
      ("epoch_1", "Screening", "Screening", screening, [encounters[0]['encounterId']]),
      ("epoch_2", "Treatment", "Treatment", treatment, encounter_ids_2),
      ("epoch_3", "Follow-up", "Follow-up", follow_up, encounter_ids_3)
    ]
    epochs = []
    for epoch in raw_epoch_data:
      epochs.append(study_epoch_data(*epoch))
    double_link(epochs, "studyEpochId", 'previousStudyEpochId', 'nextStudyEpochId')

    # <<<<< Rules need updatting >>>>>
    # Elements
    # Fields: name, description, start rule, end rule
    raw_element_data = [
      ("study_element_1", "Screening", "Screening", rules[0], rules[4]),
      ("study_element_2", "Treatment", "Tocilizumab in combination with standard of care", None, None),
      ("study_element_3", "Palcebo", "Placebo in combination with standard of care", None, None),
      ("study_element_4", "Follow Up", "Follow up", None, None),
    ]
    elements = []
    for element in raw_element_data:
      elements.append(study_element_data(*element[0:3], start=element[3], end=element[4]))

    # Study Cells
    study_cells = []
    study_cells.append(study_cell_data("study_cell_1", study_arm_1, epochs[0], [ elements[0] ]))
    study_cells.append(study_cell_data("study_cell_2", study_arm_1, epochs[1], [ elements[1] ]))
    study_cells.append(study_cell_data("study_cell_3", study_arm_1, epochs[2], [ elements[3] ]))
    study_cells.append(study_cell_data("study_cell_4", study_arm_2, epochs[0], [ elements[0] ]))
    study_cells.append(study_cell_data("study_cell_5", study_arm_2, epochs[1], [ elements[2] ]))
    study_cells.append(study_cell_data("study_cell_6", study_arm_2, epochs[2], [ elements[3] ]))

    # <<<<< Need setting up >>>>>
    # Study Design
    intent = code_for('StudyDesign', 'trialIntentType', submission_value='CURE')
    design_type = code_for('StudyDesign', 'trialType', submission_value='EFFICACY')
    int_model = code_for('StudyDesign', 'interventionModel', submission_value='SEQUENTIAL')
    ta = code_data("123456789", "SNOMED", "2022", "Something")
    therapeutic_areas = [ta]
    timeline = schedule_timeline_data("timeline_1", "Timeline 1", "The first timeline", "Condition for Entry", "timeline_entry_1")
    design_1 = study_design_data("study_design_1", "Study Design 1", "The first study design", [intent], [design_type], int_model, therapeutic_areas, study_cells, indications, objectives, [study_population_1], ii, [timeline], estimands, [], [], "Study Design rationale")
    designs = [design_1]

    # Protocol versions
    # Fields: brief_title, official_title, public_title, scientific_title, version, amendment, effective_date, status):
    draft_status = code_for('StudyProtocolVersion', 'protocolStatus', submission_value='Draft')
    protocol_version_1 = study_protocol_version_data(
      "study_protocol_version_1",
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
    organisation_1 = organization_data("organization_1", "DUNS", "482242971", "F. Hoffmann-la Roche Ag", sponsor_type)
    organisation_2 = organization_data("organization_2", "USGOV", "CT-GOV", "ClinicalTrials.gov", registry_type)
    organisation_3 = organization_data("organization_3", "EMA", "EudraCT", "European Union Drug Regulating Authorities Clinical Trials Database", regulator_type)
    identifier_1 = study_identifier_data("study_identifier_1", "WA42380", organisation_1)
    identifier_2 = study_identifier_data("study_identifier_2", "NCT04320615", organisation_2)
    identifier_3 = study_identifier_data("study_identifier_3", "2020-001154-22", organisation_3)
    identifiers = [identifier_1, identifier_2, identifier_3]

    # Assemble complete study
    study_title = "Tocilizumab in Patients With Severe COVID-19 Pneumonia"
    phase = alias_code_data("alias_1", code_data("C49686", "http://www.cdisc.org", "2022-03-25", "Phase III Trial"))
    study_type = code_data("C98388", "http://www.cdisc.org", "2022-03-25", "Interventional Study")
    bta = code_data("12345", "Sponsor", "2022", "Business Unit A")
    business_therapeutic_areas = [bta]
    return study_data(study_title, "1", study_type, phase, business_therapeutic_areas, identifiers, protocol_versions, designs)

