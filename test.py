import sys
from service.service import Service
from study.simple_study import *
from study.ddr import *

studies = [
  SimpleStudy, 
  DDR
  ]
items = [
  "studies", "study_identifiers", "organisations", "study_protocol_versions", "study_arms", "study_epochs", 
  "study_cells", "study_elements", "codes", "study_data", "procedures", "activities", "transition_rules", "encounters"
  ]
  
if __name__ == "__main__":
  service = Service(sys.argv)
  # for study in studies:
  #   data = study.json()
  #   uuid = service.post("study_definitions", data)
  #   service.get("study_definitions", uuid)
  #   service.get("studies", uuid)
  # for item in items:
  #  uuids = service.get("%s/list" % (item))
  #  service.get(item, uuids[0])
  identifiers = ["ACME-5678", "NCT04298023"]
  for identifier in identifiers:
    uuid = service.get("study_definitions?identifier=%s" % (identifier))
    study_designs = service.get("study_designs?study_uuid=%s" % (uuid))
    soa = service.get("study_designs/soa/%s" % (study_designs[0]['uuid']))
  