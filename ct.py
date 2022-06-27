import os
import requests
import yaml

API_KEY = os.getenv('CDISC_API_KEY')

def get_code_list(releases, c_code):
  for release in releases:
    headers =  {"Content-Type":"application/json", "api-key": API_KEY}
    api_url = "https://api.library.cdisc.org/api/mdr/ct/packages/%s/codelists/%s" % (release, c_code)
    response = requests.get(api_url, headers=headers)
    body = response.json()
    if response.status_code == 200:
      return body 
  return None

c_code_list = {
  'Study': {
    'studyType': "C99077", 
    'studyPhase': "C66737"
  },
  'StudyDesign': {
    'trialIntentType': "C66736", 
    'trialType': "C66739",
    'interventionModel': 'C99076'
  },
  'StudyArm': {
    'studyArmType': 'C174222'
  },
  'StudyEpoch': {
    'studyEpochType': 'C99079'
  },
  'Encounter': {
    'encounterEnvironmentalSetting': 'C127262',
    'encounterContactMode': 'C171445'
  }
}
releases = ["sdtmct-2022-03-25", "protocolct-2022-03-25"]
result = {}

for klass, info in c_code_list.items():
  result[klass] = {}
  for attribute, c_code in info.items():
    print("Working ...")
    body = get_code_list(releases, c_code)
    body.pop('_links', None)
    result[klass][attribute] = body

print(result)
with open('data/ct.yaml', 'w') as outfile:
  yaml.dump(result, outfile, default_flow_style=False)

