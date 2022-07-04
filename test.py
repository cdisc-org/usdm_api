import sys
from service.service import Service
from study.simple_study import *
from study.ddr import *
import pandas as pd
from pandas import json_normalize

studies = [ SimpleStudy, DDR ]
identifiers = ["NCT04298023", "ACME-5678"] 
  
if __name__ == "__main__":
  service = Service(sys.argv)
  # for study in studies:
  #   data = study.json()
  #   uuid = service.post("studyDefinitions", data)
  for identifier in identifiers:
    uuid = service.get("studyDefinitions?identifier=%s" % (identifier))
    identifiers = service.get("studyIdentifiers?study_uuid=%s" % (uuid))
    service.get("studyDefinitions", uuid)
    study_designs = service.get("studyDesigns?study_uuid=%s" % (uuid))
    soa = service.get("studyDesigns/%s/soa" % (study_designs[0]['uuid']))
    df = json_normalize(soa)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.max_colwidth', None)
    print(df)