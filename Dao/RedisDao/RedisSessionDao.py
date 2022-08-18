from .Connection import RedisHandler
from .RedisDaoBase import RedisSessionBaseDao
from DataModels.RedisModels import RedisJsonSessions, RedisSession
from APIsMaker.RedisAPIs.KeySchema import CourseSessionJsonKeySchema


class RedisSessionDao(RedisSessionBaseDao):

    RedisPipelines = RedisHandler.pipeline()

    def _convertRedisJsonSessionToDict(self,sessionJson: RedisJsonSessions) -> dict:
        RedisSesionsDict = {}
        for session in sessionJson.sessions:
            RedisSesionsDict[session.id] = session.session.dict()
        return RedisSesionsDict

    def _confirmJsonCreation(self, key: str, keyExists: bool) -> None:
        if not keyExists:
            EmptyDict = {}
            self.RedisPipelines.json().set(key,".", EmptyDict)

    def _preparingRedisPipes(self, key: str, RedisSesionsDict: dict ) -> None:
        for k,v in RedisSesionsDict.items():
            s = str("." +str(k)).replace(" ", "")
            self.RedisPipelines.json().set(key, s, v)

    def _checkJsonExists(self, key) -> bool:
        return RedisHandler.exists(key)


    def addMember(self,sessionJson: RedisJsonSessions) -> None:
        key = CourseSessionJsonKeySchema(sessionJson.runID)
        RedisSesionsDict = self._convertRedisJsonSessionToDict(sessionJson)
        KeyExists = self._checkJsonExists(key)
        self._confirmJsonCreation(key, KeyExists)
        self._preparingRedisPipes(key , RedisSesionsDict)
        self.RedisPipelines.execute()

    def _convertDictToRedisSessionJson(self,RedisSesionsDict : dict, runId: str ) ->RedisJsonSessions :
        RedisSessionsList = []
        for SessionKey, SessionValue in RedisSesionsDict.items():
            RedisSessionsList.append(RedisSession(id=SessionKey, session=SessionValue))
        RedisJsonSessionObject = RedisJsonSessions(sessions=RedisSessionsList, runID=runId)
        return RedisJsonSessionObject

    def retrieveMember(self, runId : str) -> RedisJsonSessions:
        key = CourseSessionJsonKeySchema(runId)
        RedisSesionsDict = RedisHandler.json().get(key , ".")
        RedisJsonResponseObject = self._convertDictToRedisSessionJson(RedisSesionsDict, runId)
        return RedisJsonResponseObject




# from DataModels.SSGModels import SSGSession,SSGVenue
# from DataModels.RedisModels import RedisSession
# obj = [SSGSession(id='Fuchun 01111s', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30',
#                   modeOfTraining='1', venue=SSGVenue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC',
#                                                      postalCode='123455', room='24', wheelChairAccess=True), attendanceTaken=False, deleted=False),
#        SSGSession(id='Fuchun 019-48', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30',
#                   modeOfTraining='1',
#                   venue=SSGVenue(block='112A', street='Street ABC', floor='18', unit='001', building='Building ABC',
#                                  postalCode='123455', room='24', wheelChairAccess=True), attendanceTaken=False, deleted=False)
#        ]
# object_dict = {x.id: x for x in obj}
# listt = []
# for k,v in object_dict.items():
#     listt.append(RedisSession(id=k , session=v))
# finalObj = RedisJsonSessions(sessions=listt , runID= "12345")
# RSD = RedisSessionDao()
# # RSD.addMember(finalObj)
# print(RSD.retrieveMember("1235"))
