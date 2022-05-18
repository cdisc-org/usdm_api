from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from store.store import Store

store = Store()

class ApiBaseModel(BaseModel):

  def check_and_save(self, item):
    if item == None:
      return None
    elif isinstance(item, str):
      return item
    else:
      return item.save()

  def save(self):
    self.uuid = str(uuid4())
    print("Class:", self.__class__.__name__)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

class Amendment(ApiBaseModel):
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
  study_protocol_amendments: Union[List[Amendment], List[str], None] = []

  def save(self):
    self.uuid = str(uuid4())
    for idx, amendment in enumerate(self.study_protocol_amendments):
      self.study_protocol_amendments[idx] = self.check_and_save(amendment)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

class Code(ApiBaseModel):
  uuid: Union[str, None] = None
  code: str
  code_system: str
  code_system_version: str
  decode: str

class StudyIdentifier(ApiBaseModel):
  uuid: Union[str, None] = None
  study_identifier_desc: str
  study_identifier_name: str
  org_code: str

class Study(ApiBaseModel):
  uuid: Union[str, None] = None
  study_title: str
  study_version: str
  study_status: str
  study_protocol_version: str
  study_type: Union[Code, str, None]
  study_phase: Union[Code, str, None]
  study_identifier: Union[List[StudyIdentifier], List[str], None] = []
  study_protocol_reference: Union[StudyProtocol, str, None] = None

  def save(self):
    self.uuid = str(uuid4())
    self.study_type = self.check_and_save(self.study_type)
    self.study_phase = self.check_and_save(self.study_phase)
    self.study_protocol_reference = self.check_and_save(self.study_protocol_reference)
    for idx, identifier in enumerate(self.study_identifier):
      self.study_identifier[idx] = self.check_and_save(identifier)
    store.put(self.__class__.__name__, vars(self), self.uuid)
    return self.uuid

app = FastAPI()

@app.get("/")
def read_root():
  return {"Version": "0.1", "System": "DDF API Simulator"}

@app.get("/study/")
def list_items():
  return store.list("Study")

@app.post("/study/")
async def create_item(study: Study):
  study.save()
  return study.uuid

@app.get("/study/{uuid}")
def read_item(uuid: str):
  return store.get("Study", uuid)

@app.post("/protocol/")
async def create_item(protocol: StudyProtocol):
  protocol.save()
  return protocol.uuid