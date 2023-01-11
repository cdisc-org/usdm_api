from .api_base_model import ApiBaseModel

class StudyData(ApiBaseModel):
  studyDataId: str
  studyDataName: str
  studyDataDescription: str
  crfLink: str
