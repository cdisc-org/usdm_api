from fastapi import FastAPI, HTTPException, status
from uuid import UUID
from store.store import Store
from model.study import *
from model.study_identifier import *
from model.organisation import *
from model.study_protocol_version import *
from model.code import *
from model.ct import *
from model.study_arm import *
from model.study_cell import *
from model.list_uuid import *

VERSION = "0.11"
SYSTEM_NAME = "DDF API Simulator"

tags_metadata = [
    {
        "name": "production",
        "description": "Routes that form the production specification."
    },
    {
        "name": "proposed",
        "description": "Routes that are proposed as being included within the production specification."
    },
    {
        "name": "potential",
        "description": "Routes that could potentially be included in the production specification."
    },
    {
        "name": "simulator",
        "description": "Routes used to support the simulator."
    }
]

annotations = {
  "study": {
    'post': {
      'summary': "Create a study",
      'description': "Create a study resource"
    },
    'get': {
      'summary': "List the studies",
      'description': "Return the identifiers for all the studies in the repository"
    },
    'get_uuid': {
      'summary': "Return a study",
      'description': "Return an study resource"
    }
  },
  "study_definition": {
    'post': {
      'summary': "Create a study",
      'description': "Create an entire study including all child element with a single post"
    },
    'get': {
      'summary': "List the studies",
      'description': "Return the identifiers for all the studies in the repository"
    },
    'get_uuid': {
      'summary': "Return a study",
      'description': "Return an entire study including all child elements"
    }
  }
}

app = FastAPI(
  title = SYSTEM_NAME,
  description = "A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository (SDR) Simulator. Used to define and test the logic of the SDR API.",
  version = VERSION,
  openapi_tags = tags_metadata
)
store = Store()

# System Name and Version
@app.get("/", 
  tags=["simulator"],
  summary="Obtain system name and version",
  description="Obtain the name of the micro service and the current version.")
@app.get("/v1/", 
  tags=["simulator"],
  summary="Obtain system name and version",
  description="Obtain the name of the micro service and the current version.")
def system_and_version():
  return { "system": SYSTEM_NAME, "version": VERSION }

# Study Definition
@app.get("/v1/study_definition/", 
  tags=["proposed"], 
  summary=annotations['study_definition']['get']['summary'],
  description=annotations['study_definition']['get']['description'], 
  response_model=ListUUID)
async def list_studies():
  return Study.list(store)

@app.post("/studydefinitionrepository/v1", 
  tags=["production"], 
  summary=annotations['study_definition']['post']['summary'],
  description=annotations['study_definition']['post']['description'], 
  status_code=status.HTTP_201_CREATED)
@app.post("/v1/study_definition/", 
  tags=["proposed"], 
  summary=annotations['study_definition']['post']['summary'],
  description=annotations['study_definition']['post']['description'], 
  status_code=status.HTTP_201_CREATED)
async def create_study(study: Study):
  study.recursive_save(store)
  return study.uuid

@app.get("/studydefinitionrepository/v1/{study}", tags=["production"], 
  summary=annotations['study_definition']['get_uuid']['summary'],
  description=annotations['study_definition']['get_uuid']['description'])
@app.get("/v1/study_definition/{uuid}", tags=["proposed"], 
  summary=annotations['study_definition']['get_uuid']['summary'],
  description=annotations['study_definition']['get_uuid']['description'])
async def read_full_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.recursive_read(store, uuid)

# Study
@app.get("/v1/study/", 
  tags=["potential"], 
  summary=annotations['study']['get']['summary'],
  description=annotations['study']['get']['description'], 
  response_model=ListUUID)
async def list_studies():
  return Study.list(store)

@app.get("/v1/study/{uuid}", 
  tags=["potential"], 
  summary=annotations['study']['get_uuid']['summary'],
  description=annotations['study']['get_uuid']['description'])
async def read_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.read(store, uuid)

# Study Identifiers
@app.get("/v1/study_identifier/", 
  tags=["potential"], 
  response_model=ListUUID
)
async def list_study_identifiers():
  return StudyIdentifier.list(store)

@app.post("/v1/study_identifier/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_identifier(identifier: StudyIdentifier):
  identifier.recursive_save(store, None)
  return identifier.uuid

@app.get("/v1/study_identifier/{uuid}", response_model=StudyIdentifier, tags=["potential"])
async def read_study_identifier(uuid: UUID):
  if str(uuid) not in StudyIdentifier.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyIdentifier.read(store, str(uuid))

# Organisations
@app.get("/v1/organisation/", 
  tags=["potential"], 
  response_model=ListUUID
)
async def list_organisations():
  return Organisation.list(store)

@app.post("/v1/organisation/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_organisation(org: Organisation):
  org.save(store, None)
  return org.uuid

@app.get("/v1/organisation/{uuid}", response_model=Organisation, tags=["potential"])
async def read_organisation(uuid: UUID):
  if str(uuid) not in Organisation.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Organisation.read(store, str(uuid))

@app.get("/v1/organisation_full/{uuid}", tags=["potential"])
async def read_organisation_full(uuid: UUID):
  if str(uuid) not in Organisation.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Organisation.recursive_read(store, str(uuid))

# Study Protocol Version
@app.get("/v1/study_protocol_version/", 
  tags=["potential"], 
  response_model=ListUUID
)
async def list_study_protocol_versions():
  return StudyProtocolVersion.list(store)

@app.post("/v1/study_protocol_version/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_protocol_version(version: StudyProtocolVersion):
  version.save(store, None)
  return version.uuid

@app.get("/v1/study_protocol_version/{uuid}", response_model=StudyProtocolVersion, tags=["potential"])
async def read_study_protocol_version(uuid: UUID):
  if str(uuid) not in StudyProtocolVersion.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyProtocolVersion.read(store, str(uuid))

# Study Arm
@app.get("/v1/study_arm/", 
  tags=["potential"], 
  response_model=ListUUID)
async def list_study_arms():
  return StudyArm.list(store)

@app.post("/v1/study_arm/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_arm(item: StudyArm):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_arm/{uuid}", response_model=StudyArm, tags=["potential"])
async def read_study_arm(uuid: UUID):
  if str(uuid) not in StudyArm.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyArm.read(store, str(uuid))

# Study Cell
@app.get("/v1/study_cell/", 
  tags=["potential"], 
  response_model=ListUUID
)
async def list_study_cells():
  return StudyCell.list(store)

@app.post("/v1/study_cell/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_cell(item: StudyCell):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_cell/{uuid}", response_model=StudyCell, tags=["potential"])
async def read_study_cell(uuid: UUID):
  if str(uuid) not in StudyCell.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyCell.read(store, str(uuid))

# Code
@app.get("/v1/code/", 
  tags=["potential"], 
  response_model=ListUUID
)
async def list_codes():
  return Code.list(store)

@app.post("/v1/code/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_code(item: Code):
  item.save(store, None)
  return item.uuid

@app.get("/v1/code/{uuid}", response_model=Code, tags=["potential"])
async def read_code(uuid: UUID):
  if str(uuid) not in Code.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Code.read(store, str(uuid))

# Controlled Terminology
@app.get("/v1/ct/", 
  tags=["potential"],
  summary="Return specified Controlled Terminology",
  description="Return the specified Controlled Terminology (CT) for the specified class and attribute. This is the CT defined within the model specification")
async def ct_search(klass: str, attribute: str):
  return CT().search(klass, attribute)