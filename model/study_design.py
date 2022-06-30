from typing import List, Union
from .api_base_model import ApiBaseModel
from .code import Code
from .study_cell import StudyCell
from .indication import Indication
from .investigational_intervention import InvestigationalIntervention
from .study_design_population import StudyDesignPopulation
from .objective import Objective
from .workflow import Workflow
from .estimand import Estimand
from uuid import UUID
import pandas as pd

class StudyDesign(ApiBaseModel):
  uuid: Union[UUID, None] = None
  trialIntentTypes: Union[List[Code], List[UUID]]
  trialType: Union[Code, UUID]
  interventionModel: Union[Code, UUID]
  studyCells: Union[List[StudyCell], List[UUID], None] = []
  studyIndications: Union[List[Indication], List[UUID], None] = []
  studyInvestigationalInterventions: Union[List[InvestigationalIntervention], List[UUID], None] = []
  studyPopulations: Union[List[StudyDesignPopulation], List[UUID], None] = []
  studyObjectives: Union[List[Objective], List[UUID], None] = []
  studyWorkflows: Union[List[Workflow], List[UUID], None] = []
  studyEstimands: Union[List[Estimand], List[UUID], None] = []

  @classmethod
  def search(cls, store, uuid):
    designs = store.get_by_klass_and_scope("StudyDesign", uuid)
    print("DESIGNS:", designs)
    return designs

class SoA():
  def __init__(self, study_design, store):
    self.study_design = study_design
    self.store = store
    self.encounters = {}
    self.activities = {}

  def soa(self):
    # Data
    visits = []
    visit_index = {}
    visit_rule = []
    epochs = []

    epochs, visits = self.epochs_and_encounters()
    for idx, visit in enumerate(visits):
        visit_index[visit] = idx

    print("SOA [1]:", epochs)
    print("SOA [2]:", visits)

    # Visit Rules
    result = self.encounter_rules()
    for record in result:
      if record["start_rule"] == record["end_rule"]:
        visit_rule.append("%s" % (record["start_rule"]))
      else:
        visit_rule.append("%s to %s" % (record["start_rule"], record["end_rule"]))

    print("SOA [3]:", visit_rule)

    # Activities
    activities = {}
    results = self.activity_encounters()
    for record in results:
      if not record["activity"] in activities:
        activities[record["activity"]] = [''] * len(visits)
      activities[record["activity"]][visit_index[record["visit"]]] = "X" 

    print("SOA [4]:", activities)

    # Activity Order
    activity_order = self.activity_order()

    print("SOA [5]:", activity_order)
  
    rows = []
    rows.append([""] + list(epochs))
    rows.append([""] + list(visits))
    rows.append([""] + list(visit_rule))
    for activity in activity_order:
      if activity in activities:
        data = activities[activity]
        rows.append([activity] + list(data))
    n = len(rows[0])
    df = pd.DataFrame(rows, columns=list(range(n)))
    print(df.to_string())
    return df

  def epochs_and_encounters(self):
    epochs = {}
    ordered_epochs = []
    encounters = {}
    ordered_encounters = []
    cells = self.store.get_by_klass("StudyCell")
    for cell in cells:
      if cell['uuid'] in map(str, self.study_design.studyCells):
        epoch_uuid = cell['studyEpoch']
        epoch = self.store.get("", epoch_uuid)
        epoch_name = epoch['studyEpochName']
        for element_uuid in cell['studyElements']:
          element = self.store.get("", element_uuid)
          for encounter_uuid in element['encounters']:
            encounter = self.store.get("", encounter_uuid)
            encounter_name = encounter['encounterName']
            ordinal = encounter['sequenceInStudyDesign']
            encounters[encounter_name] = int(ordinal)
            epochs[encounter_name] = epoch_name
            self.encounters[encounter_name] = encounter
            for activity_uuid in encounter['activities']:
              activity = self.store.get("", activity_uuid)
              self.activities[activity['activityDesc']] = activity
    ordered_encounters = self.order_dict(encounters)
    for encounter in ordered_encounters:
      ordered_epochs.append(epochs[encounter])
    return ordered_epochs, ordered_encounters

  def encounter_rules(self):
    the_encounters = []
    #encounters = store.get_by_klass_and_scope("Encounter", str(self.uuid))
    for encounter in self.encounters.values():
      encounter_name = encounter['encounterName']
      start_rule_uuid = encounter['transitionStartRule']
      end_rule_uuid = encounter['transitionEndRule']
      ordinal = encounter['sequenceInStudyDesign']
      record = { 
        'visit': encounter_name, 
        'ordinal': int(ordinal), 
        'start_rule': self.get_rule(start_rule_uuid), 
        'end_rule': self.get_rule(end_rule_uuid) 
      }
      the_encounters.append(record)
    return sorted(the_encounters, key = lambda i: i['ordinal'])

  def get_rule(self, uuid):
    if uuid == None:
      return ""
    rule = self.store.get("", uuid)['transitionRuleDesc']
    return rule

  def activity_encounters(self):
    activities = []
    #encounters = store.get_by_klass_and_scope("Encounter", str(self.uuid))
    for encounter in self.encounters.values():
      encounter_name = encounter['encounterName']
      for activity_uuid in encounter['activities']:
        activity = self.store.get("", activity_uuid)
        activities.append({ 'visit': encounter_name, 'activity': activity['activityDesc'] })
    return activities

  def activity_order(self):
    the_activities = {}
    #activities = store.get_by_klass_and_scope("Activity", str(self.uuid))
    for activity in self.activities.values():
      ordinal = activity['sequenceInStudyDesign']
      desc = activity['activityDesc']
      the_activities[desc] = int(ordinal)
    ordered = self.order_dict(the_activities)
    return ordered.keys()

  def order_dict(self, the_dict):
    return { k: the_dict[k] for k in sorted(the_dict, key=the_dict.get) }