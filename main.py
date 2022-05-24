from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from store.store import Store
from model.api_base_model import ApiBaseModel
from model.study import Study
from model.study_protocol import StudyProtocol

VERSION = "0.3"
SYSTEM_NAME = "DDF API Simulator"

app = FastAPI()
the_store = Store()

@app.get("/")
def read_root():
  return {"Version":VERSION, "System": SYSTEM_NAME}

@app.get("/study/")
def list_items():
  return the_store.list("Study")

@app.post("/study/")
async def create_item(study: Study):
  study.recursive_save(the_store)
  return study.uuid

@app.get("/study_full/{uuid}")
def read_full_item(uuid: str):
  return Study.recursive_read(uuid, the_store)

@app.get("/study/{uuid}")
def read_item(uuid: str):
  return Study.read(uuid, the_store)

#@app.post("/protocol/")
#async def create_item(protocol: StudyProtocol):
#  protocol.save(the_store)
#  return protocol.uuid