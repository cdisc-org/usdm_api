from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import *
from .study_protocol_version import *
from .code import *
from .study_design import *
from uuid import UUID
import pandas as pd

class Study(ApiBaseModel):
  uuid: Union[UUID, None]
  studyTitle: str
  studyVersion: str
  studyType: Union[Code, UUID, None]
  studyPhase: Union[Code, UUID, None]
  studyIdentifiers: Union[List[StudyIdentifier], List[UUID], None] = []
  studyProtocolVersions: Union[List[StudyProtocolVersion], List[UUID], None] = []
  studyDesigns: Union[List[StudyDesign], List[UUID], None] = []

  @classmethod
  def scope_reuse(cls):
    return False
  
  @classmethod
  def search(cls, store, identifier):
    identifiers = store.get_by_klass("StudyIdentifier")
    for item in identifiers:
      result = store.get("", item['uuid'])
      if result['studyIdentifier'] == identifier:
        studies = store.get_by_klass("Study")
        for study in studies:
          if result['uuid'] in study['studyIdentifiers']:
            return study['uuid']
    return None

  def soa(self, store):
    # Data
    visits = []
    visit_index = {}
    visit_rule = []
    epochs = []

    epochs, visits = self.epochs_and_encounters(store)
    for idx, visit in enumerate(visits):
        visit_index[visit] = idx

    # Visit Rules
    result = self.encounter_rules(store)
    for record in result:
      if record["start_rule"] == record["end_rule"]:
        visit_rule.append("%s" % (record["start_rule"]))
      else:
        visit_rule.append("%s to %s" % (record["start_rule"], record["end_rule"]))

    # Activities
    activities = {}
    results = self.activity_encounters(store)
    for record in results:
      if not record["activity"] in activities:
        activities[record["activity"]] = [''] * len(visits)
      activities[record["activity"]][visit_index[record["visit"]]] = "X" 

    # Activity Order
    activity_order = self.activity_order(store)
  
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

  def epochs_and_encounters(self, store):
    epochs = {}
    ordered_epochs = []
    encounters = {}
    ordered_encounters = []
    cells = store.get_by_klass_and_scope("StudyCell", str(str(str(self.uuid))))
    for cell in cells:
      epoch_uuid = cell['studyEpoch']
      epoch = store.get("", epoch_uuid)
      epoch_name = epoch['studyEpochName']
      for element_uuid in cell['studyElements']:
        element = store.get("", element_uuid)
        for encounter_uuid in element['encounters']:
          encounter = store.get("", encounter_uuid)
          encounter_name = encounter['encounterName']
          ordinal = encounter['sequenceInStudy']
          epochs[encounter_name] = epoch_name
          encounters[encounter_name] = int(ordinal)
    ordered_encounters = self.order_dict(encounters)
    for encounter in ordered_encounters:
      ordered_epochs.append(epochs[encounter])
    return ordered_epochs, ordered_encounters

  def encounter_rules(self, store):
    the_encounters = []
    encounters = store.get_by_klass_and_scope("Encounter", str(self.uuid))
    for encounter in encounters:
      encounter_name = encounter['encounterName']
      start_rule_uuid = encounter['transitionStartRule']
      end_rule_uuid = encounter['transitionEndRule']
      ordinal = encounter['sequenceInStudy']
      record = { 
        'visit': encounter_name, 
        'ordinal': int(ordinal), 
        'start_rule': self.get_rule(store, start_rule_uuid), 
        'end_rule': self.get_rule(store, end_rule_uuid) 
      }
      the_encounters.append(record)
    return sorted(the_encounters, key = lambda i: i['ordinal'])

  def get_rule(self, store, uuid):
    if uuid == None:
      return ""
    rule = store.get("", uuid)['transitionRuleDesc']
    return rule

  def activity_encounters(self, store):
    activities = []
    encounters = store.get_by_klass_and_scope("Encounter", str(self.uuid))
    for encounter in encounters:
      encounter_name = encounter['encounterName']
      for activity_uuid in encounter['activities']:
        activity = store.get("", activity_uuid)
        activities.append({ 'visit': encounter_name, 'activity': activity['activityDesc'] })
    return activities

  def activity_order(self, store):
    the_activities = {}
    activities = store.get_by_klass_and_scope("Activity", str(self.uuid))
    for activity in activities:
      ordinal = activity['sequenceInStudy']
      desc = activity['activityDesc']
      the_activities[desc] = int(ordinal)
    ordered = self.order_dict(the_activities)
    return ordered.keys()

  def order_dict(self, the_dict):
    return { k: the_dict[k] for k in sorted(the_dict, key=the_dict.get) }