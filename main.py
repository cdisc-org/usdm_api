from fastapi import FastAPI, HTTPException, status, Response
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
from model.transition_rule import *
from model.encounter import *

#VERSION = "0.22"
VERSION = "V1-Provisional"
SYSTEM_NAME = "Simple API for DDF"

tags_metadata = [
    {
        "name": "Production",
        "description": "Routes that form the production specification."
    },
    # {
    #     "name": "proposed",
    #     "description": "Routes that are proposed as being included within the production specification."
    # },
    # {
    #     "name": "SoA",
    #     "description": "Routes related to the SoA for a study design."
    # },
    # {
    #     "name": "Search",
    #     "description": "Routes related to search functions."
    # },
    # {
    #     "name": "Sections",
    #     "description": "Routes providing similar functionality to that of 'sections' in the previous draft of the API."
    # },
    # {
    #     "name": "potential",
    #     "description": "Routes that could potentially be included in the production specification. These tend to be more granular routes, more typical 'resource' driven."
    # },
    # {
    #     "name": "Simulator",
    #     "description": "Routes used to support the simulator, not for production."
    # }
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

standard_response_fields = {
  "status_code": "string",
  "detail": "string",
  "message": "string"
}

standard_responses = {
  400: standard_response_fields,
  401: standard_response_fields
}

app = FastAPI(
  title = SYSTEM_NAME,
  description = "A simple TransCelerate Digital Data Flow (DDF) Study Definitions Repository API.",
  version = VERSION,
  openapi_tags = tags_metadata
)
store = Store()

# System Name and Version
# @app.get("/", 
#   tags=["Simulator"],
#   summary="Obtain system name and version",
#   description="Obtain the name of the micro service and the current version.")
# @app.get("/v1/", 
#   tags=["Simulator"],
#   summary="Obtain system name and version",
#   description="Obtain the name of the micro service and the current version.")
# def system_and_version():
#   return { "system": SYSTEM_NAME, "version": VERSION }

# Controlled Terminology
# @app.get("/v1/terms/", 
#   tags=["Simulator"],
#   summary="Return Controlled Terminology",
#   description="Return the specified Controlled Terminology (CT) for the specified class and attribute. This is the CT defined within the model specification")
# async def ct_search(klass: str, attribute: str):
#   return CT().search(klass, attribute)
  
# Study Definition
# @app.get("/v1/study_definitions/list", 
#   tags=["proposed"], 
#   summary=annotations['study_definition']['get']['summary'],
#   description=annotations['study_definition']['get']['description'], 
#   response_model=List[UUID])
# async def list_studies():
#   return Study.list(store)

# @app.get("/v1/studyDefinitions", 
#   tags=['Search'], 
#   summary='Study definition for specified identifier',
#   description='Returns the uuid for the study with the matching identifier.',
#   response_model=UUID)
# async def studies_search(identifier: str=""):
#   result = Study.search(store, identifier)
#   if result == None:
#     raise HTTPException(status_code=404, detail="Item not found")
#   return result

# @app.post("/studydefinitionrepository/v1", 
#   tags=["production"], 
#   summary=annotations['study_definition']['post']['summary'],
#   description=annotations['study_definition']['post']['description'], 
#   status_code=status.HTTP_201_CREATED,
#   response_model=UUID)
@app.post("/v1/studyDefinitions", 
  tags=["Production"], 
  summary=annotations['study_definition']['post']['summary'],
  description=annotations['study_definition']['post']['description'], 
  status_code=status.HTTP_201_CREATED,
  response_model=UUID,
  responses=standard_responses)
async def create_study(study: Study):
  study.recursive_save(store)
  return study.uuid

# @app.get("/studydefinitionrepository/v1/{study}", tags=["production"], 
#   summary=annotations['study_definition']['get_uuid']['summary'],
#   description=annotations['study_definition']['get_uuid']['description'])
@app.get("/v1/studyDefinitions/{uuid}", 
  tags=["Production"], 
  summary=annotations['study_definition']['get_uuid']['summary'],
  description=annotations['study_definition']['get_uuid']['description'],
  responses=standard_responses)
async def read_full_study(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=404, detail="Item not found")
  return Study.recursive_read(store, uuid)

@app.get("/v1/studyDefinitions/{uuid}/history", 
  tags=["Production"], 
  summary="",
  description="",
  response_model=List[Study],
  responses=standard_responses)
async def read_study_history(uuid: str):
  if uuid not in Study.list(store):
    raise HTTPException(status_code=501, detail="Not implemented")
  return []

# Study
# @app.get("/v1/studies/list", 
#   tags=["potential"], 
#   summary=annotations['study']['get']['summary'],
#   description=annotations['study']['get']['description'], 
#   response_model=List[UUID])
# async def list_studies():
#   return Study.list(store)

# @app.get("/v1/studies/{uuid}", 
#   tags=["potential"], 
#   summary=annotations['study']['get_uuid']['summary'],
#   description=annotations['study']['get_uuid']['description'])
# async def read_study(uuid: str):
#   if uuid not in Study.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   return Study.read(store, uuid)

# Study Identifiers
# @app.get("/v1/study_identifiers/list", 
#   tags=["potential"],
#   response_model=List[UUID]
# )
# async def list_study_identifiers():
#   return StudyIdentifier.list(store)

# @app.get("/v1/studyIdentifiers", 
#   tags=["Sections"], 
#   summary='Study identifiers for a study',
#   description='Returns all the identifiers for a specified study.',
#   response_model=List[StudyIdentifier]
# )
# async def study_identifiers_search(study_uuid: UUID):
#   return StudyIdentifier.search(store, str(study_uuid))

# @app.post("/v1/study_identifiers", 
#   tags=["potential"], 
#   status_code=status.HTTP_201_CREATED)
# async def create_study_identifier(identifier: StudyIdentifier):
#   identifier.recursive_save(store, None)
#   return identifier.uuid

# @app.get("/v1/study_identifiers/{uuid}", response_model=StudyIdentifier, tags=["potential"])
# async def read_study_identifier(uuid: UUID):
#   if str(uuid) not in StudyIdentifier.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   return StudyIdentifier.read(store, str(uuid))

# Organisations
# @app.get("/v1/organisations/list", 
#   tags=["potential"], 
#   response_model=List[UUID]
# )
# async def list_organisations():
#   return Organisation.list(store)

# @app.post("/v1/organisations", 
#   tags=["potential"], 
#   status_code=status.HTTP_201_CREATED)
# async def create_organisation(org: Organisation):
#   org.save(store, None)
#   return org.uuid

# @app.get("/v1/organisations/{uuid}", response_model=Organisation, tags=["potential"])
# async def read_organisation(uuid: UUID):
#   if str(uuid) not in Organisation.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   return Organisation.read(store, str(uuid))

# @app.get("/v1/organisation_full/{uuid}", tags=["potential"])
# async def read_organisation_full(uuid: UUID):
#   if str(uuid) not in Organisation.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   return Organisation.recursive_read(store, str(uuid))

# Study Protocol Version
# @app.get("/v1/study_protocol_versions/list", 
#   tags=["potential"], 
#   response_model=List[UUID]
# )
# async def list_study_protocol_versions():
#   return StudyProtocolVersion.list(store)

# @app.post("/v1/study_protocol_versions", 
#   tags=["potential"], 
#   status_code=status.HTTP_201_CREATED)
# async def create_protocol_version(version: StudyProtocolVersion):
#   version.save(store, None)
#   return version.uuid

# @app.get("/v1/study_protocol_versions/{uuid}", response_model=StudyProtocolVersion, tags=["potential"])
# async def read_study_protocol_version(uuid: UUID):
#   if str(uuid) not in StudyProtocolVersion.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   return StudyProtocolVersion.read(store, str(uuid))

# Study Design
# @app.get("/v1/study_designs/list", 
#   tags=["potential"], 
#   response_model=List[UUID])
# async def list_study_designs():
#   return StudyDesign.list(store)

# @app.post("/v1/study_designs", 
#   tags=["potential"], 
#   status_code=status.HTTP_201_CREATED)
# async def create_study_design(item: StudyDesign):
#   item.save(store, None)
#   return item.uuid

# @app.get("/v1/study_designs/{uuid}", response_model=StudyDesign, tags=["potential"])
# async def read_study_design(uuid: UUID):
#   if str(uuid) not in StudyDesign.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   return StudyDesign.read(store, str(uuid))

@app.get("/v1/studyDesigns", 
  tags=['Production'],
  summary='Study designs for a study',
  description='Returns all the study designs for a specified study.',
  response_model=List[StudyDesign],
  responses=standard_responses
)
async def search_study_design(study_uuid: UUID):
  return StudyDesign.search(store, str(study_uuid))

# @app.get("/v1/studyDesigns/{uuid}/soa", 
#   tags=["SoA"],
#   summary='SoA for the specified study design',
#   description='Returns a SoA for the specified study design. The SoA returned is a JSON structure (pandas dataframe to JSON) representing the SoA for the study.',
#   responses=standard_responses
# )
# async def studies_soa(uuid: UUID):
#   if str(uuid) not in StudyDesign.list(store):
#     raise HTTPException(status_code=404, detail="Item not found")
#   study_design = StudyDesign(**StudyDesign.read(store, str(uuid)))
#   df = SoA(study_design, store).soa()
#   return Response(df.to_json(orient="records"), media_type="application/json")
