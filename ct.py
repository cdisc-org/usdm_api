import os
import requests
import yaml

API_KEY = os.getenv('CDISC_API_KEY')

c_code_list = {
  'Study': {
    'study_type': "C66737", 
    'study_phase': "C99077"
  }
}
sdtm_release = "sdtmct-2022-03-25"
result = {}

headers =  {"Content-Type":"application/json", "api-key": API_KEY}
for klass, info in c_code_list.items():
  result[klass] = {}
  for attribute, c_code in info.items():
    api_url = "https://api.library.cdisc.org/api/mdr/ct/packages/%s/codelists/%s" % (sdtm_release, c_code)
    response = requests.get(api_url, headers=headers)
    body = response.json()
    body.pop('_links', None)
    result[klass][attribute] = body

print(result)
with open('data/ct.yaml', 'w') as outfile:
  yaml.dump(result, outfile, default_flow_style=False)


