import abc
from DataModels.SSGModels import Session as SSGSession
from DataModels.TadaBaseModels import Session as TadaBaseSession
from DataModels.TadaBaseModels import Venue as TadaBaseVenue

class SSGToTadaBaseMapperBase(abc.ABC):
    @abc.abstractmethod
    def DataModelSessionMapper(self,ssgsession: SSGSession) -> [TadaBaseSession,TadaBaseVenue]:
        pass