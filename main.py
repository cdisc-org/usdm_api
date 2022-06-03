from typing import List, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID
from store.store import Store
from model.api_base_model import ApiBaseModel
from model.study import Study
from model.study_identifier import *
from model.organisation import *
from model.study_protocol_version import *
from model.code import *

VERSION = "0.5"
SYSTEM_NAME = "DDF API Simulator"

app = FastAPI()
store = Store()

@app.get("/")
def read_root():
  return {"Version":VERSION, "System": SYSTEM_NAME}

@app.get("/study/")
def list_studies():
  return Study.list(store)

@app.post("/study/")
async def create_study(study: Study):
  study.recursive_save(store)
  return study.uuid

@app.get("/study_full/{uuid}")
def read_full_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.recursive_read(store, uuid)

@app.get("/study/{uuid}")
def read_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.read(store, uuid)

@app.get("/study_identifier/")
def list_study_identifiers():
  return StudyIdentifier.list(store)

@app.post("/study_identifier/")
async def create_study_identifier(identifier: StudyIdentifier):
  identifier.recursive_save(store, None)
  return identifier.uuid

@app.get("/study_identifier/{uuid}", response_model=StudyIdentifierResponse)
def read_study_identifier(uuid: UUID):
  if str(uuid) not in StudyIdentifier.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyIdentifier.read(store, str(uuid))

@app.get("/study_identifier_full/{uuid}")
def read_study_identifier(uuid: UUID):
  if str(uuid) not in StudyIdentifier.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyIdentifier.recursive_read(store, str(uuid))

@app.get("/organisation/")
def list_organisations():
  return Organisation.list(store)

@app.post("/organisation/")
async def create_organisation(org: Organisation):
  org.save(store, None)
  return org.uuid

@app.get("/organisation/{uuid}", response_model=OrganisationResponse)
def read_organisation(uuid: UUID):
  if str(uuid) not in Organisation.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Organisation.read(store, str(uuid))

@app.get("/organisation_full/{uuid}")
def read_organisation_full(uuid: UUID):
  if str(uuid) not in Organisation.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Organisation.recursive_read(store, str(uuid))

@app.get("/study_protocol_version/")
def list_study_protocol_versions():
  return StudyProtocolVersion.list(store)

@app.post("/study_protocol_version/")
async def create_protocol_version(version: StudyProtocolVersion):
  version.save(store, None)
  return version.uuid

@app.get("/study_protocol_version/{uuid}", response_model=StudyProtocolVersionResponse)
def read_study_protocol_version(uuid: UUID):
  if str(uuid) not in StudyProtocolVersion.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyProtocolVersion.read(store, str(uuid))

@app.get("/code/")
def list_codes():
  return Code.list(store)

@app.post("/code/")
async def create_code(item: Code):
  item.save(store, None)
  return item.uuid

@app.get("/code/{uuid}", response_model=CodeResponse)
def read_code(uuid: UUID):
  if str(uuid) not in Code.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Code.read(store, str(uuid))
