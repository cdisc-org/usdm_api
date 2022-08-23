import sys
from service.service import Service
from study.simple_study import *
from study.ddr import *
from study.bms import *
import pandas as pd
from pandas import json_normalize
import json

studies = [ SimpleStudy, DDR, BMS ]
identifiers = ["NCT04298023", "ACME-5678", "XYZ01235"] 

def save_as_file(data, filename):
  with open('study/%s.json' % (filename), 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=2)

if __name__ == "__main__":
  service = Service(sys.argv)
  service.get("")
  # for study in studies:
  #    data = study.json()
  #    save_as_file(data, study.__name__)
  #    uuid = service.post("studyDefinitions", data)
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