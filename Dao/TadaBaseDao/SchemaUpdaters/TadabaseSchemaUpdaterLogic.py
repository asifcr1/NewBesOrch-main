import requests
import json
import abc

from APIsMaker.TadaBaseAPIs.APISchema import ListFieldsInTableSchema
from DataModels.TadaBaseModels import Field

class TadaBaseTableSchemaBase(abc.ABC):
    @abc.abstractmethod
    def update_schema(self,tableId) -> str:
        pass


class TadaBaseTableSchema(TadaBaseTableSchemaBase):

    def _retreive_fields(self, TableAPIUrl, AppHeaders, RequestPayload) -> [Field]:
        FieldsResponse = requests.request("GET", TableAPIUrl,headers=AppHeaders,data=RequestPayload)
        FieldsDict = json.loads(FieldsResponse.text)
        FieldsObjects = [Field.parse_obj(FieldMember) for FieldMember in FieldsDict["fields"]]
        return FieldsObjects

    def _extract_schema(self,FieldsObjects: [Field]) -> dict:
        SchemaDict = {}
        for FieldObject in FieldsObjects:
            SchemaDict[FieldObject.name] = FieldObject.slug
        return SchemaDict

    def _save_schema(self, SchemaDict: dict, FileName: str) -> str:
        FullPath = "Storage/" + FileName
        with open(FullPath, 'w') as fp:
            json.dump(SchemaDict, fp)
        return FullPath

    def update_schema(self,tableId: str, AppHeaders: dict, FileName:str) -> str:
        TableAPIUrl , RequestPayload  = ListFieldsInTableSchema(tableId)
        FieldsObjects = self._retreive_fields(TableAPIUrl , AppHeaders , RequestPayload)
        TableSchema = self._extract_schema(FieldsObjects)
        FilePath = self._save_schema(TableSchema, FileName)
        return FilePath

