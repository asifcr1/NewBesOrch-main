import requests
import ast
from .TadabaseBaseDao import TadaBaseSessionBaseDao
from DataModels.TadaBaseModels import Session, SessionResponse, insertResponse
from APIsMaker.TadaBaseAPIs.APISchema import InsertRecordsSchema
from APIsMaker.TadaBaseAPIs.APITableConfig import courseSessionJaafarTableId
from APIsMaker.TadaBaseAPIs.APIAppConfig import BESTrainingHeadersConfig
from Mappers.GeneralMapper import create_tadabase_insert_payload

# from DataModels.SSGModels import Session as SSGSession
# from DataModels.TadaBaseModels import SessionReponse
# from Mappers.SSGToTadabaseMapper import SSGToTadabaseMapper
# import pandas as pd
# import json
# from APIsMaker.TadaBaseAPIs.APISchema import  retrieveRecordsSchema
# from APIsMaker.TadaBaseAPIs.APITableConfig import  venueJaafarTableId




class TadaBaseSessionDao(TadaBaseSessionBaseDao):

    def insert(self, session: Session) -> SessionResponse:
        headers = BESTrainingHeadersConfig()
        tableId = courseSessionJaafarTableId()
        APIEndPoint = InsertRecordsSchema(tableId)
        SessionPayload = create_tadabase_insert_payload(r"C:\Users\User\Work\Orch\BESOrchestrator\Schemas\TadaBase\Storage\CourseSessionJaafar",session.dict())
        SessionResponseBack = requests.request("POST", APIEndPoint, headers=headers, data=SessionPayload)
        finalResponse = SessionResponse(session=session,TadaBaseResponse=insertResponse.parse_obj(ast.literal_eval(SessionResponseBack.text)))
        return finalResponse

    # def _checkSession(self, session: SSGSession , IdField: str) -> bool:
    #     Checker = False
    #     headers = BESTrainingHeadersConfig()
    #     tableId = courseSessionJaafarTableId()
    #     APIEndPoint, payload = retrieveRecordsSchema(tableId)
    #     SessionResponse = requests.request("GET", APIEndPoint, headers=headers, data=payload)
    #     df = pd.DataFrame(ast.literal_eval(SessionResponse.text)['items'])
    #     if (not df.empty) and (session.id in df[IdField].tolist()):
    #         Checker= True
    #     return Checker



    # def insertFromSSG(self, session: SSGSession) -> str:
    #     with open("../../Schemas/TadaBase/Storage/CourseSessionJaafar", "r") as fp:
    #         fields = json.load(fp)
    #     if self._checkSession(session, fields['id']):
    #         raise Exception('Session Found already!')
    #     headers = BESTrainingHeadersConfig()
    #     tableId = venueJaafarTableId()
    #     APIEndPoint = InsertRecordsSchema(tableId)
    #     Mapper = SSGToTadabaseMapper()
    #     TBSession, TBVenue = Mapper.DataModelSessionMapper(session)
    #     VenuePayload = create_tadabase_insert_payload("../../Schemas/TadaBase/Storage/VenueJaafar" , TBVenue.dict())
    #     VenueResponse = requests.request("POST", APIEndPoint, headers=headers, data=VenuePayload)
    #     VenueResponse = VenueResponse.text
    #     VenueResponse = ast.literal_eval(VenueResponse)
    #     tableId = courseSessionJaafarTableId()
    #     APIEndPoint = InsertRecordsSchema(tableId)
    #     TBSession.venue = VenueResponse['recordId']
    #     SessionPayload = create_tadabase_insert_payload("../../Schemas/TadaBase/Storage/CourseSessionJaafar", TBSession.dict())
    #     SessionResponse = requests.request("POST", APIEndPoint, headers=headers, data=SessionPayload)
    #     sessionResponse = SessionReponse(session=TBSession, venue=TBVenue,TadaBaseResponse=ast.literal_eval(SessionResponse.text))
    #     return sessionResponse

# obj = Session(id='Fuchun 019-41618-S1', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30', modeOfTraining='1', venue='22', attendanceTaken=False, deleted=False)
# TBS = TadaBaseSessionDao()
# res = TBS.insert(obj)
# print(res)
# print(res.dict())