from typing import List, Union
from .api_base_model import ApiBaseModel
from .study_identifier import *
from .study_protocol_version import *
from .code import *
from .study_design import *
from uuid import UUID

class Study(ApiBaseModel):
  uuid: Union[UUID, None]
  studyTitle: str
  studyVersion: str
  studyType: Union[Code, None]
  studyPhase: Union[Code, None]
  studyIdentifiers: Union[List[StudyIdentifier], List[UUID], None] = []
  studyProtocolVersions: Union[List[StudyProtocolVersion], List[UUID], None] = []
  studyDesigns: Union[List[StudyDesign], List[UUID], None] = []

  @classmethod
  def scope_reuse(cls):
    return False
  
  @classmethod
  def search(cls, store, identifier):
    identifiers = store.get_by_klass("StudyIdentifier")
    print(identifiers)
    for item in identifiers:
      result = store.get("", item['uuid'])
      print(result)
      print(result['studyIdentifier'])
      print(identifier)
      if result['studyIdentifier'] == identifier:
        print("found")
        return store.scope(item['uuid'])
    return None
