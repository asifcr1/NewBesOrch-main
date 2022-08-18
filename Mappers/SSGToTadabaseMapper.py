from typing import Union
from .DataModelsMappersBase import SSGToTadaBaseMapperBase

from DataModels.SSGModels import SSGSession as SSGSession
from DataModels.TadaBaseModels import Session as TadaBaseSession
from DataModels.TadaBaseModels import Venue as TadaBaseVenue

class SSGToTadabaseMapper(SSGToTadaBaseMapperBase):
    def DataModelSessionMapper(self, ssgsession: SSGSession) -> Union[TadaBaseSession, TadaBaseVenue]:
        TadaBaseVenueDict = ssgsession.venue.dict()
        ssgsession.venue = "0"
        TadaBaseSessionDict = ssgsession.dict()
        TBVenue = TadaBaseVenue.parse_obj(TadaBaseVenueDict)
        TBSession = TadaBaseSession.parse_obj(TadaBaseSessionDict)
        return TBSession , TBVenue



