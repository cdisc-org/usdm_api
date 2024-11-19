from typing import List, Union, Literal
from .api_base_model import ApiBaseModelWithIdNameLabelAndDesc
from .identifier import MedicalDeviceIdentifier
from .comment_annotation import CommentAnnotation

class MedicalDevice(ApiBaseModelWithIdNameLabelAndDesc):
  hardwareVersion: Union[str, None] = None
  softwareVersion: Union[str, None] = None
  embeddedProductId: Union[str, None] = None
  identifiers: List[MedicalDeviceIdentifier] = []
  notes: List[CommentAnnotation] = []
  instanceType: Literal['MedicalDevice']
