from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from store.store import Store

store = Store()

class Amendment(BaseModel):
  uuid: Union[str, None] = None
  amendment_effective_date: str
  amendment_version: str

class StudyProtocol(BaseModel):
  uuid: Union[str, None] = None
  brief_title: str
  full_title: str
  public_title: str
  scientific_title: str
  version: str
  study_protocol_amendments: Union[List[Amendment], None] = []

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
  study_protocol_reference: Union[str, None] = None
  #study_status: Union[str, None] = None

app = FastAPI()

@app.get("/")
def read_root():
  return {"Version": "0.1", "System": "DDF API Simulator"}

@app.get("/study/{uuid}")
def read_item(uuid: str):
  return store.get("Study", uuid)

@app.get("/study/")
def read_item():
  return store.list("Study")

@app.post("/study/")
async def create_item(study: Study):
  study.uuid = str(uuid4())
  study.study_type.uuid = str(uuid4())
  study.study_phase.uuid = str(uuid4())
  for identifier in study.study_identifier:
    identifier.uuid = str(uuid4())
  store.put("Study", vars(study), study.uuid)
  return study.uuid

@app.post("/protocol/")
async def create_item(protocol: StudyProtocol):
  protocol.uuid = str(uuid4())
  for amendment in protocol.study_protocol_amendments:
    amendment.uuid = str(uuid4())
  store.put("Protocol", vars(protocol), protocol.uuid)
  return protocol.uuid