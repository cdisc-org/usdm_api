from typing import List, Union
from fastapi import FastAPI
from deta import Deta
from pydantic import BaseModel
from uuid import uuid4

deta = None
ddf_store = None

def init_store():
  global ddf_store
  global deta
  try: 
    deta = Deta()
    ddf_store = deta.Base("ddf_store")
  except:
    deta = None
    ddf_store = {}

def store_put(data, key):
  global ddf_store
  global deta
  if deta == None:
    #print("%s -> %s" % (key, data))
    ddf_store[key] = data
  else:
    ddf_store.put(data, key)

def store_get(key):
  global ddf_store
  global deta
  if deta == None:
    #print("%s" % (key))
    return ddf_store[key]
  else:
    return ddf_store.get(key)

init_store()

class Code(BaseModel):
  uuid: Union[str, None] = None
  code: str
  code_system: str
  code_system_version: str
  decode: str

class StudyIdentifier(BaseModel):
  uuid: Union[str, None] = None
  study_identifier_desc: str
  study_identifier_name: str
  org_code: str

class Study(BaseModel):
  uuid: Union[str, None] = None
  study_title: str
  study_version: str
  study_status: str
  study_protocol_version: str
  study_type: Code
  study_phase: Code
  study_identifier: Union[List[StudyIdentifier], None] = []
  #study_status: Union[str, None] = None

app = FastAPI()

@app.get("/")
def read_root():
  return {"Version": "0.1", "System": "DDF API Simulator"}

@app.get("/study/{uuid}")
def read_item(uuid: str):
  return store_get(uuid)

@app.post("/study/")
async def create_item(study: Study):
  study.uuid = str(uuid4())
  study.study_type.uuid = str(uuid4())
  study.study_phase.uuid = str(uuid4())
  #for identifier in study.identifiers:
  #  identifier.uuid = str(uuid4())
  store_put(vars(study), study.uuid)
  return study.uuid