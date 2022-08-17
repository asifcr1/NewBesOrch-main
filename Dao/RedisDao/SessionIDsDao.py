from .Connection import RedisHandler
from .RedisDaoBase import SessionIDsDaoBase
from DataModels.RedisModels import SessionIDTadaBase
from APIsMaker.RedisAPIs.KeySchema import HashedIDsTadaBaseSchema

class SessionIDsDao(SessionIDsDaoBase):

    def addMember(self,sessionIdObj: SessionIDTadaBase) -> None:
        key = HashedIDsTadaBaseSchema("session")
        RedisHandler.hset(key, mapping={sessionIdObj.sessionId : sessionIdObj.TadaBaseRecordId})

    def checkExist(self, sessionID: str) -> bool:
        key = HashedIDsTadaBaseSchema("session")
        return RedisHandler.hexists(key, sessionID )

    def retrieveRecordIdfromSessionId(self, sessionID: str) -> str:
        key = HashedIDsTadaBaseSchema("session")
        return RedisHandler.hget(key, sessionID)





