from .Connection import RedisHandler
from .RedisDaoBase import VenueIDsDaoBase
from DataModels.RedisModels import VenueIDTadaBase
from APIsMaker.RedisAPIs.KeySchema import HashedIDsTadaBaseSchema


class VenueIDsDao(VenueIDsDaoBase):

    def addMember(self,venueIdObj: VenueIDTadaBase ) -> None:
        key = HashedIDsTadaBaseSchema("venue")
        RedisHandler.hset(key, mapping={venueIdObj.venueObject : venueIdObj.TadaBaseRecordId})

    def checkExist(self, venueObject: str) -> bool:
        key = HashedIDsTadaBaseSchema("venue")
        return RedisHandler.hexists(key, venueObject)

    def retrieveRecordIdfromSessionId(self, venueObject: str) -> str:
        key = HashedIDsTadaBaseSchema("venue")
        return RedisHandler.hget(key, venueObject)





#
# obj = VenueIDTadaBase(venueObject="4342" , TadaBaseRecordId="jfeo")
# VID = VenueIDsDao()
# VID.addMember(obj)
# print(VID.checkExist("1234"))
# print(VID.retrieveRecordIdfromSessionId("1234"))