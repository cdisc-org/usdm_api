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
        return store.scope(item['uuid'])
    return None

  def soa(self, store):
    # Data
    visits = {}
    visit_row = {}
    visit_rule = {}
    epoch_visits = {}
    epoch_count = 0

    epoch_visits, visits = self.epochs_and_encounters(store)
    for visit in visits:
      visit_row[visit] = ""

    # Visit Rules
    result = self.encounter_rules(store)
    for visit in visits.keys():
      visit_rule[visit] = ""
    for record in result:
      if record["start_rule"] == record["end_rule"]:
        visit_rule[record["visit"]] = "%s" % (record["start_rule"])
      else:
        visit_rule[record["visit"]] = "%s to %s" % (record["start_rule"], record["end_rule"])

    # Activities
    activities = {}
    results = self.activity_encounters(store)
    for record in results:
      if not record["activity"] in activities:
        activities[record["activity"]] = visit_row.copy()
      activities[record["activity"]][record["visit"]] = "X" 

    # Activity Order
    activity_order = self.activity_order(store)
  
    rows = []
    rows.append([""] + list(visits.values()))
    rows.append([""] + list(visits.keys()))
    rows.append([""] + list(visit_rule.values()))
    for activity in activity_order:
      if activity in activities:
        data = activities[activity]
        rows.append([activity] + list(data.values()))
    n = len(rows[0])
    df = pd.DataFrame(rows, columns=list(range(n)))
    print(df.to_string())
    return df

  def epochs_and_encounters(self, store):
    epochs = {}
    encounters = {}
    cells = store.get_by_klass_and_scope("StudyCell", str(str(str(self.uuid))))
    for cell in cells:
      epoch_uuid = cell['studyEpoch']
      epoch = store.get("", epoch_uuid)
      epoch_name = epoch['studyEpochName']
      epochs[epoch_name] = []
      for element_uuid in cell['studyElements']:
        element = store.get("", element_uuid)
        for encounter_uuid in element['encounters']:
          encounter = store.get("", encounter_uuid)
          encounter_name = encounter['encounterName']
          epochs[epoch_name].append(encounter_name)
          encounters[encounter_name] = epoch_name
    return epochs, encounters

  def encounter_rules(self, store):
    the_encounters = []
    encounters = store.get_by_klass_and_scope("Encounter", str(self.uuid))
    for encounter in encounters:
      encounter_name = encounter['encounterName']
      start_rule_uuid = encounter['transitionStartRule']
      end_rule_uuid = encounter['transitionEndRule']
      the_encounters.append({ 'visit': encounter_name, 'start_rule': self.get_rule(store, start_rule_uuid), 'end_rule': self.get_rule(store, end_rule_uuid) })
    return the_encounters

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
    the_activities = []
    activities = store.get_by_klass_and_scope("Activity", str(self.uuid))
    for activity in activities:
      ordinal = activity['sequenceInStudy']
      the_activities.insert(int(ordinal) - 1,activity['activityDesc'])
    return the_activities