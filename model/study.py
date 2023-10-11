from typing import List, Union
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .study_protocol_document import StudyProtocolDocument
from .study_version import StudyVersion

class Study(ApiBaseModelWithIdNameLabelAndDesc):
  versions: List[StudyVersion] = []
  documentedBy: Union[StudyProtocolDocument, None] = None
  