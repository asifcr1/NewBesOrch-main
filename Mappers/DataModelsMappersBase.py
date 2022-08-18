import abc
from DataModels.SSGModels import SSGSession as SSGSession
from DataModels.TadaBaseModels import Session as TadaBaseSession
from DataModels.TadaBaseModels import Venue as TadaBaseVenue
from DataModels.RedisModels import RedisJsonSessions

class SSGToTadaBaseMapperBase(abc.ABC):
    @abc.abstractmethod
    def DataModelSessionMapper(self,ssgsession: SSGSession) -> [TadaBaseSession,TadaBaseVenue]:
        pass

class SSGToRedisMapperBase(abc.ABC):
    @abc.abstractmethod
    def DataModelSessionsMapper(self,ssgsessions: [SSGSession]) -> RedisJsonSessions:
        pass