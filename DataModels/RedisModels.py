from pydantic import BaseModel
from .GeneralModels import Session
from typing import List


class SessionIDTadaBase(BaseModel):
    sessionId: str
    TadaBaseRecordId : str


class VenueIDTadaBase(BaseModel):
    venueObject: str
    TadaBaseRecordId : str


class RedisSession(BaseModel):
    id : str
    session : Session


class RedisJsonSessions(BaseModel):
    runID: str
    sessions: List[RedisSession]

# from GeneralModels import Venue
# obj = Session(id='Fuchun 019-41-S', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30', modeOfTraining='1', venue=Venue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC', postalCode='12345', room='24', wheelChairAccess=True), attendanceTaken=False, deleted=False)
#
# obj2 = RedisSession(session= obj, updated='d')
# print(obj2)