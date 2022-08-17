import abc
from DataModels.SSGModels import *


class SSGSessionBaseDao(abc.ABC):
    @abc.abstractmethod
    def retrieve(self, course_run_id) -> [Session]:
        pass

