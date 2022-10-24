import sys
from study.simple_study import *
from study.ddr import *
from study.bms import *
from study.Roche_WA42380 import *
import pandas as pd
from pandas import json_normalize
import json

#studies = [ SimpleStudy, DDR, BMS, RocheWA42380 ]
studies = [ SimpleStudy, DDR ] #, RocheWA42380 ]

def save_as_file(data, filename):
  with open('study/%s.json' % (filename), 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=2)

if __name__ == "__main__":
  for study in studies:
    data = study.json()
    save_as_file(data, study.__name__)
