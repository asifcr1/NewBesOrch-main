import abc
from DataModels.SSGModels import SSGSessionResponse


class SSGSessionBaseDao(abc.ABC):
    @abc.abstractmethod
    def retrieve(self, course_run_id: str) -> SSGSessionResponse:
        pass

