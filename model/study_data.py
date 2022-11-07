from .api_base_model import ApiBaseModel

class StudyData(ApiBaseModel):
  studyDataId: str
  studyDataName: str
  studyDataDesc: str
  crfLink: str
