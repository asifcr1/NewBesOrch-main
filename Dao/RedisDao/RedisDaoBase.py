import abc
from DataModels.RedisModels import RedisJsonSessions


class RedisSessionBaseDao(abc.ABC):
    @abc.abstractmethod
    def addMember(self,sessions: RedisJsonSessions) -> None:
        pass
    @abc.abstractmethod
    def retrieveMember(self, runId : str) -> RedisJsonSessions:
        pass



# class SessionIDsDaoBase(abc.ABC):
#     @abc.abstractmethod
#     def addMember(self,sessionIdObj: SessionIDTadaBase) -> None:
#         pass
#
#     @abc.abstractmethod
#     def checkExist(self, sessionID: str) -> bool:
#         pass
#
#     @abc.abstractmethod
#     def retrieveRecordIdfromSessionId(self, sessionID: str) -> str:
#         pass
#
#
# class VenueIDsDaoBase(abc.ABC):
#     @abc.abstractmethod
#     def addMember(self,venueIdObj: VenueIDTadaBase ) -> None:
#         pass
#
#     @abc.abstractmethod
#     def checkExist(self, venueObject: str) -> bool:
#         pass
#
#     @abc.abstractmethod
#     def retrieveRecordIdfromSessionId(self, venueObject: str) -> str:
#         pass



