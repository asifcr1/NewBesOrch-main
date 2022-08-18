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



# import time
#
#
# obj = VenueIDTadaBase(venueObject="4342" , TadaBaseRecordId="jfeo")
# VID = VenueIDsDao()
# start_time = time.time()
# VID.addMember(obj)
# print("Adding member to Redis --- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# VID.checkExist("1234")
# print("Checking for a key in Redis --- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# VID.retrieveRecordIdfromSessionId("1234")
# print("Retrieving a key value from Redis --- %s seconds ---" % (time.time() - start_time))