import requests
import ast
from .TadabaseBaseDao import TadaBaseVenueBaseDao
from DataModels.TadaBaseModels import Venue, VenueResponse, insertResponse
from APIsMaker.TadaBaseAPIs.APISchema import InsertRecordsSchema
from APIsMaker.TadaBaseAPIs.APIAppConfig import BESTrainingHeadersConfig
from APIsMaker.TadaBaseAPIs.APITableConfig import  venueJaafarTableId
from Mappers.GeneralMapper import create_tadabase_insert_payload


class TadaBaseVenueDao(TadaBaseVenueBaseDao):

    def insert(self, venue: Venue) -> VenueResponse:
        headers = BESTrainingHeadersConfig()
        tableId = venueJaafarTableId()
        APIEndPoint = InsertRecordsSchema(tableId)
        VenuePayload = create_tadabase_insert_payload(r"C:\Users\User\Work\Orch\BESOrchestrator\Schemas\TadaBase\Storage\VenueJaafar", venue.dict())
        VenueResponseBack = requests.request("POST", APIEndPoint, headers=headers, data=VenuePayload)
        finalResponse = VenueResponse(venue=venue, TadaBaseResponse=insertResponse.parse_obj(ast.literal_eval(VenueResponseBack.text)))
        return finalResponse

# obj = Venue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC', postalCode='123455', room='24', wheelChairAccess=True)