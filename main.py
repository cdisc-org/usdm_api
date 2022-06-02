from typing import List, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID
from store.store import Store
from model.api_base_model import ApiBaseModel
from model.study import Study
from model.study_identifier import *
from model.organisation import *

VERSION = "0.3"
SYSTEM_NAME = "DDF API Simulator"

app = FastAPI()
the_store = Store()

@app.get("/")
def read_root():
  return {"Version":VERSION, "System": SYSTEM_NAME}

@app.get("/study/")
def list_studies():
  return the_store.list("Study")

@app.post("/study/")
async def create_study(study: Study):
  study.recursive_save(the_store)
  return study.uuid

@app.get("/study_full/{uuid}")
def read_full_study(uuid: str):
  if uuid not in the_store.list("Study"):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.recursive_read(uuid, the_store)

@app.get("/study/{uuid}")
def read_study(uuid: str):
  if uuid not in the_store.list("Study"):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.read(uuid, the_store)

@app.get("/study_identifier/")
def list_study_identifiers():
  return the_store.list("StudyIdentifier")

@app.post("/study_identifier/")
async def create_study_identifier(identifier: StudyIdentifier):
  identifier.recursive_save(the_store)
  return identifier.uuid

@app.get("/study_identifier/{uuid}", response_model=StudyIdentifierResponse)
def read_study_identifier(uuid: UUID):
  if str(uuid) not in the_store.list("StudyIdentifier"):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyIdentifier.read(str(uuid), the_store)

@app.get("/organisation/")
def list_organisations():
  return the_store.list("Organisation")

@app.post("/organisation/")
async def create_organisation(org: Organisation):
  org.recursive_save(the_store)
  return org.uuid

@app.get("/organisation/{uuid}", response_model=OrganisationResponse)
def read_organisation(uuid: UUID):
  print("A", the_store.list("Organisation"))
  if str(uuid) not in the_store.list("Organisation"):
    raise HTTPException(status_code=404, detail="Item not found")
  return Organisation.read(str(uuid), the_store)

@app.get("/organisation_full/{uuid}", response_model=OrganisationResponse)
def read_organisation_full(uuid: UUID):
  print("A", the_store.list("Organisation"))
  if str(uuid) not in the_store.list("Organisation"):
    raise HTTPException(status_code=404, detail="Item not found")
  return Organisation.recursive_read(str(uuid), the_store)
