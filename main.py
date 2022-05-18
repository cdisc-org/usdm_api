from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from store.store import Store
from model.api_base_model import ApiBaseModel
from model.study import Study
from model.study_protocol import StudyProtocol

app = FastAPI()
the_store = Store()

@app.get("/")
def read_root():
  return {"Version": "0.1", "System": "DDF API Simulator"}

@app.get("/study/")
def list_items():
  return the_store.list("Study")

@app.post("/study/")
async def create_item(study: Study):
  study.save(the_store)
  return study.uuid

@app.get("/study/{uuid}")
def read_item(uuid: str):
  return the_store.get("Study", uuid)

@app.post("/protocol/")
async def create_item(protocol: StudyProtocol):
  protocol.save(the_store)
  return protocol.uuid