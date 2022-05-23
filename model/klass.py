from .amendment import Amendment
from .code import Code
from .indication import Indication
from .rule import Rule
from .study_arm import StudyArm
from .study_cell import StudyCell
from .study_design import StudyDesign
from .study_element import StudyElement
from .study_epoch import StudyEpoch
from .study_identifier import StudyIdentifier
from .study_protocol import StudyProtocol
from .study import Study

class Klass():

  def get(name):
    return globals()[name]
