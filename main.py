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
from model.study_data import *
from model.procedure import *
from model.activity import *

VERSION = "0.12"
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
@app.get("/v1/study_definitions/", 
  tags=["proposed"], 
  summary=annotations['study_definition']['get']['summary'],
  description=annotations['study_definition']['get']['description'], 
  response_model=List[UUID])
async def list_studies():
  return Study.list(store)

@app.post("/studydefinitionrepository/v1", 
  tags=["production"], 
  summary=annotations['study_definition']['post']['summary'],
  description=annotations['study_definition']['post']['description'], 
  status_code=status.HTTP_201_CREATED,
  response_model=UUID)
@app.post("/v1/study_definitions/", 
  tags=["proposed"], 
  summary=annotations['study_definition']['post']['summary'],
  description=annotations['study_definition']['post']['description'], 
  status_code=status.HTTP_201_CREATED,
  response_model=UUID)
async def create_study(study: Study):
  study.recursive_save(store)
  return study.uuid

@app.get("/studydefinitionrepository/v1/{study}", tags=["production"], 
  summary=annotations['study_definition']['get_uuid']['summary'],
  description=annotations['study_definition']['get_uuid']['description'])
@app.get("/v1/study_definitions/{uuid}", tags=["proposed"], 
  summary=annotations['study_definition']['get_uuid']['summary'],
  description=annotations['study_definition']['get_uuid']['description'])
async def read_full_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.recursive_read(store, uuid)

# Study
@app.get("/v1/studies/", 
  tags=["potential"], 
  summary=annotations['study']['get']['summary'],
  description=annotations['study']['get']['description'], 
  response_model=List[UUID])
async def list_studies():
  return Study.list(store)

@app.get("/v1/studies/{uuid}", 
  tags=["potential"], 
  summary=annotations['study']['get_uuid']['summary'],
  description=annotations['study']['get_uuid']['description'])
async def read_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.read(store, uuid)

# Study Identifiers
@app.get("/v1/study_identifiers/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_study_identifiers():
  return StudyIdentifier.list(store)

@app.post("/v1/study_identifiers/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_identifier(identifier: StudyIdentifier):
  identifier.recursive_save(store, None)
  return identifier.uuid

@app.get("/v1/study_identifiers/{uuid}", response_model=StudyIdentifier, tags=["potential"])
async def read_study_identifier(uuid: UUID):
  if str(uuid) not in StudyIdentifier.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyIdentifier.read(store, str(uuid))

# Organisations
@app.get("/v1/organisations/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_organisations():
  return Organisation.list(store)

@app.post("/v1/organisations/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_organisation(org: Organisation):
  org.save(store, None)
  return org.uuid

@app.get("/v1/organisations/{uuid}", response_model=Organisation, tags=["potential"])
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
@app.get("/v1/study_protocol_versions/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_study_protocol_versions():
  return StudyProtocolVersion.list(store)

@app.post("/v1/study_protocol_versions/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_protocol_version(version: StudyProtocolVersion):
  version.save(store, None)
  return version.uuid

@app.get("/v1/study_protocol_versions/{uuid}", response_model=StudyProtocolVersion, tags=["potential"])
async def read_study_protocol_version(uuid: UUID):
  if str(uuid) not in StudyProtocolVersion.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyProtocolVersion.read(store, str(uuid))

# Study Arm
@app.get("/v1/study_arms/", 
  tags=["potential"], 
  response_model=List[UUID])
async def list_study_arms():
  return StudyArm.list(store)

@app.post("/v1/study_arms/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_arm(item: StudyArm):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_arms/{uuid}", response_model=StudyArm, tags=["potential"])
async def read_study_arm(uuid: UUID):
  if str(uuid) not in StudyArm.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyArm.read(store, str(uuid))

# Study Epoch
@app.get("/v1/study_epochs/", 
  tags=["potential"], 
  response_model=List[UUID])
async def list_study_epochs():
  return StudyEpoch.list(store)

@app.post("/v1/study_epochs/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_arm(item: StudyEpoch):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_epochs/{uuid}", response_model=StudyEpoch, tags=["potential"])
async def read_study_arm(uuid: UUID):
  if str(uuid) not in StudyEpoch.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyEpoch.read(store, str(uuid))

# Study Cell
@app.get("/v1/study_cells/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_study_cells():
  return StudyCell.list(store)

@app.post("/v1/study_cells/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_cell(item: StudyCell):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_cells/{uuid}", response_model=StudyCell, tags=["potential"])
async def read_study_cell(uuid: UUID):
  if str(uuid) not in StudyCell.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyCell.read(store, str(uuid))

# Study Element
@app.get("/v1/study_elements/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_study_elements():
  return StudyElement.list(store)

@app.post("/v1/study_elements/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_cell(item: StudyElement):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_elements/{uuid}", response_model=StudyElement, tags=["potential"])
async def read_study_cell(uuid: UUID):
  if str(uuid) not in StudyElement.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyElement.read(store, str(uuid))

# Code
@app.get("/v1/codes/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_codes():
  return Code.list(store)

@app.post("/v1/codes/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_code(item: Code):
  item.save(store, None)
  return item.uuid

@app.get("/v1/codes/{uuid}", response_model=Code, tags=["potential"])
async def read_code(uuid: UUID):
  if str(uuid) not in Code.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Code.read(store, str(uuid))

# Study Data
@app.get("/v1/study_data/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_study_data():
  return StudyData.list(store)

@app.post("/v1/study_data/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_study_data(item: StudyData):
  item.save(store, None)
  return item.uuid

@app.get("/v1/study_data/{uuid}", response_model=StudyData, tags=["potential"])
async def read_study_data(uuid: UUID):
  if str(uuid) not in StudyData.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return StudyData.read(store, str(uuid))

# Procedures
@app.get("/v1/procedures/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_procedures():
  return Procedure.list(store)

@app.post("/v1/procedures/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_procedure(item: Procedure):
  item.save(store, None)
  return item.uuid

@app.get("/v1/procedures/{uuid}", response_model=Procedure, tags=["potential"])
async def read_procedure(uuid: UUID):
  if str(uuid) not in Procedure.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Procedure.read(store, str(uuid))

# Activities
@app.get("/v1/activities/", 
  tags=["potential"], 
  response_model=List[UUID]
)
async def list_activities():
  return Activity.list(store)

@app.post("/v1/activities/", 
  tags=["potential"], 
  status_code=status.HTTP_201_CREATED)
async def create_activity(item: Activity):
  item.save(store, None)
  return item.uuid

@app.get("/v1/activities/{uuid}", response_model=Activity, tags=["potential"])
async def read_activity(uuid: UUID):
  if str(uuid) not in Activity.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Activity.read(store, str(uuid))

# Controlled Terminology
@app.get("/v1/terms/", 
  tags=["potential"],
  summary="Return Controlled Terminology",
  description="Return the specified Controlled Terminology (CT) for the specified class and attribute. This is the CT defined within the model specification")
async def ct_search(klass: str, attribute: str):
  return CT().search(klass, attribute)