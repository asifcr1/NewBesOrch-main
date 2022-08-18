import abc
from DataModels.SSGModels import SSGSession as SSGSession
from DataModels.DataRoutersModels import TadaBaseSessionModelResponse


class SSGTadaBaseSession(abc.ABC):
    @abc.abstractmethod
    def insertSSGToTadaBase(self, session: SSGSession) -> TadaBaseSessionModelResponse:
        pass


