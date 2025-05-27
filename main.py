from fastapi import FastAPI, status
from model.study_version import *
from model.wrapper import Wrapper
from uuid import UUID, uuid4

VERSION = "4.0.0"
SYSTEM_NAME = "DDF USDM API"

tags_metadata = [
    {
        "name": "Production",
        "description": "Routes that form the production specification."
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
    'put': {
      'summary': "Update a study",
      'description': "Update an entire study including all child element with a single put"
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

@app.post("/v4/studyDefinitions", 
  tags=["Production"], 
  summary=annotations['study_definition']['post']['summary'],
  description=annotations['study_definition']['post']['description'], 
  status_code=status.HTTP_201_CREATED,
  response_model=UUID,
  responses=standard_responses)
async def create_study(study: Wrapper):
  return str(uuid4())

@app.put("/v4/studyDefinitions/{studyId}", 
  tags=["Production"], 
  summary=annotations['study_definition']['put']['summary'],
  description=annotations['study_definition']['put']['description'], 
  status_code=status.HTTP_200_OK,
  response_model=UUID,
  responses=standard_responses)
async def update_study(studyId: str, study: Wrapper):
  return studyId

@app.get("/v4/studyDefinitions/{studyId}", 
  tags=["Production"], 
  summary=annotations['study_definition']['get_uuid']['summary'],
  description=annotations['study_definition']['get_uuid']['description'],
  response_model=Wrapper,
  responses=standard_responses)
async def read_full_study(studyId: str):
  return {}

@app.get("/v4/studyDefinitions/{studyId}/history", 
  tags=["Production"], 
  summary="Returns the study history",
  description="Returns the history for the specified study",
  response_model=List[Wrapper],
  responses=standard_responses)
async def read_study_history(studyId: str):
  return []

@app.get("/v4/studyDesigns", 
  tags=['Production'],
  summary='Study designs for a study',
  description='Returns all the study designs for a specified study.',
  response_model=List[Union[InterventionalStudyDesign, ObservationalStudyDesign]],
  responses=standard_responses
)
async def search_study_design(studyId: UUID):
  return []
