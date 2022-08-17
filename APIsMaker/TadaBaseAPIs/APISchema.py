from typing import Union


main_enrty = "https://api.tadabase.io/api/v1/data-tables"

def ListFieldsInTableSchema(tableId: str) -> Union[str,dict]:
    api = f'https://api.tadabase.io/api/v1/data-tables/{tableId}/fields'
    payload = {}
    return api , payload

def InsertRecordsSchema(tableId: str) -> str:
    api = f'https://api.tadabase.io/api/v1/data-tables/{tableId}/records'
    return api

def retrieveRecordsSchema(tableId: str) -> Union[str,dict]:
    api = f'https://api.tadabase.io/api/v1/data-tables/{tableId}/records'
    payload = {}
    return api, payload
