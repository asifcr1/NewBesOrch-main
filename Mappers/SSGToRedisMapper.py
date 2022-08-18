from .DataModelsMappersBase import SSGToRedisMapperBase
from DataModels.SSGModels import SSGSessionResponse
from DataModels.RedisModels import RedisJsonSessions, RedisSession


class SSGToRedisMapper(SSGToRedisMapperBase):
    def DataModelSessionsMapper(self, ssgsessions: SSGSessionResponse) -> RedisJsonSessions:
        SSGSessionsDict = {ssgsession.id: ssgsession for ssgsession in ssgsessions.sessions}
        SSGSessionList = []
        for SessionKey, SessionValue in SSGSessionsDict.items():
            SSGSessionList.append(RedisSession(id=SessionKey, session=SessionValue))
        RedisJsonSessionObject = RedisJsonSessions(sessions=SSGSessionList, runID=ssgsessions.runID)
        return RedisJsonSessionObject


# from DataModels.SSGModels import SSGSession, SSGVenue
# obj = SSGSessionResponse(runID='12345', sessions=[SSGSession(id='Fuchun 019-41618-S1', startDate='20190814', endDate='20190814',
#                         startTime='15:30', endTime='17:30', modeOfTraining='1', attendanceTaken=False, deleted=False,
#                         venue=SSGVenue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC',
#                         postalCode='123455', room='24', wheelChairAccess=True)) ,
#                                                   SSGSession(id='Fuchun 019-41618-S1', startDate='20190814',
#                                                              endDate='20190814',
#                                                              startTime='15:30', endTime='17:30', modeOfTraining='1',
#                                                              attendanceTaken=False, deleted=False,
#                                                              venue=SSGVenue(block='112A', street='Street ABC',
#                                                                             floor='15', unit='001',
#                                                                             building='Building ABC',
#                                                                             postalCode='123455', room='24',
#                                                                             wheelChairAccess=True))
#                                                   , SSGSession(id='Fuchun 019-4118-S1', startDate='20190814', endDate='20190814',
#                         startTime='15:30', endTime='17:30', modeOfTraining='1', attendanceTaken=False, deleted=False,
#                         venue=SSGVenue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC',
#                         postalCode='123455', room='24', wheelChairAccess=True)),
#                                                   SSGSession(id='Fuchun 019-18-S1', startDate='20190814',
#                                                              endDate='20190814',
#                                                              startTime='15:30', endTime='17:30', modeOfTraining='1',
#                                                              attendanceTaken=False, deleted=False,
#                                                              venue=SSGVenue(block='112A', street='Street ABC',
#                                                                             floor='15', unit='001',
#                                                                             building='Building ABC',
#                                                                             postalCode='123455', room='24',
#                                                                             wheelChairAccess=True))
#                                                   ])
# SRM = SSGToRedisMapper()
# print(SRM.DataModelSessionsMapper(obj))
