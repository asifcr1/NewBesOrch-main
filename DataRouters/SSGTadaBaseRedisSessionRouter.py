from DataRoutersBased import SSGTadaBaseSession
from DataModels.SSGModels import Session as SSGSession
from DataModels.TadaBaseModels import Session as TadaBaseSession
from DataModels.TadaBaseModels import Venue as TadaBaseVenue
from DataModels.DataRoutersModels import SessionResponse, VenueResponse, TadaBaseSessionModelResponse
from DataModels.RedisModels import SessionIDTadaBase, VenueIDTadaBase
from Dao.TadaBaseDao.TadaBaseSessionDao import TadaBaseSessionDao
from Dao.TadaBaseDao.TadaBaseVenueDao import TadaBaseVenueDao
from Dao.RedisDao.SessionIDsDao import SessionIDsDao
from Dao.RedisDao.VenueIDsDao import VenueIDsDao
from Mappers.SSGToTadabaseMapper import SSGToTadabaseMapper



class SSGTadaBaseSessionRouter(SSGTadaBaseSession):

    SID = SessionIDsDao()
    VID = VenueIDsDao()
    TBSObj = TadaBaseSessionDao()
    TBVObj = TadaBaseVenueDao()
    Mapper = SSGToTadabaseMapper()

    def _updateSessionIDs(self,SessionResponseBack: SessionResponse) -> None:
        sessionIDTB = SessionIDTadaBase(sessionId=SessionResponseBack.session.id, TadaBaseRecordId=SessionResponseBack.TadaBaseResponse.recordId)
        self.SID.addMember(sessionIDTB)

    def _checkSessionID(self, session : TadaBaseSession) -> bool:
        return self.SID.checkExist(session.id)

    def _updateSessionVenue(self, VenueResponseBack : VenueResponse) -> None:
        stringVenue = "".join(VenueResponseBack.venue.dict().values())
        venueIDTB = VenueIDTadaBase(venueObject=stringVenue , TadaBaseRecordId=VenueResponseBack.TadaBaseResponse.recordId)
        self.VID.addMember(venueIDTB)

    def _checkVenueID(self, venue : TadaBaseVenue) -> bool:
        return self.VID.checkExist("".join(venue.dict().values()))

    def _retreiveExistingVenueID(self, venue : TadaBaseVenue) -> str:
        return self.VID.retrieveRecordIdfromSessionId("".join(venue.dict().values()))

    def insertSSGToTadaBase(self, session: SSGSession) -> TadaBaseSessionModelResponse:
        TBSession, TBVenue = self.Mapper.DataModelSessionMapper(session)
        if self._checkSessionID(TBSession):
            raise Exception(TBSession.id + " is already there!")
        if self._checkVenueID(TBVenue):
            TBSession.venue = self._retreiveExistingVenueID(TBVenue)
            VenueResponseBack = {'msg' : 'Venue was not add, because it is already there!' , 'recordId' :TBSession.venue }
        else:
            VenueResponseBack = self.TBVObj.insert(venue=TBVenue)
            self._updateSessionVenue(VenueResponseBack)
            TBSession.venue = VenueResponseBack.TadaBaseResponse.recordId
        SessionResponseBack = self.TBSObj.insert(session=TBSession)
        self._updateSessionIDs(SessionResponseBack)
        FinalResponse = TadaBaseSessionModelResponse(sessionResponse=SessionResponseBack , venueResponse=VenueResponseBack)
        return FinalResponse


# from DataModels.SSGModels import Venue as SSGVenue
# import time
# obj = SSGSession(id='Fuchun 019-41-S', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30', modeOfTraining='1', venue=SSGVenue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC', postalCode='12345', room='24', wheelChairAccess=True), attendanceTaken=False, deleted=False)
# start_time = time.time()
# STSR = SSGTadaBaseSessionRouter()
# print(STSR.insertSSGToTadaBase(obj))
# print("--- %s seconds ---" % (time.time() - start_time))
