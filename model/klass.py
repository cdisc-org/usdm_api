from .activity import Activity
from .amendment import Amendment
from .code import Code
from .encounter import *
from .endpoint import *
from .estimand import *
from .indication import Indication
from .intercurrent_event import *
from .investigational_intervention import *
from .objective import *
from .point_in_time import *
from .population import *
from .procedure import *
from .rule import Rule
from .study_arm import StudyArm
from .study_cell import StudyCell
from .study_data import *
from .study_design import StudyDesign
from .study_element import StudyElement
from .study_epoch import StudyEpoch
from .study_identifier import StudyIdentifier
from .study_protocol import StudyProtocol
from .study import Study
from .workflow import *
from .workflow_item import *

class Klass():

  def get(name):
    return globals()[name]
