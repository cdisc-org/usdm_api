import sys
from service.service import Service
from study.simple_study import *
from study.ddr import *

studies = [
  #SimpleStudy, 
  DDR
  ]
items = [
  "studies", "study_identifiers", "organisations", "study_protocol_versions", "study_arms", "study_epochs", 
  "study_cells", "study_elements", "codes", "study_data", "procedures", "activities", "transition_rules", "encounters"
  ]
  
if __name__ == "__main__":
  service = Service(sys.argv)
  for study in studies:
    uuid = service.post("study_definitions", study.json())
    service.get("study_definitions", uuid)
    service.get("studies", uuid)
  for item in items:
    uuids = service.get(item)
    service.get(item, uuids[0])
