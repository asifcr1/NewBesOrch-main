from Dao.TadaBaseDao.SchemaUpdaters.TadabaseSchemaUpdaterLogic import TadaBaseTableSchema

from APIsMaker.TadaBaseAPIs.APIAppConfig import BESTrainingHeadersConfig
from APIsMaker.TadaBaseAPIs.APITableConfig import courseSessionTableId, courseSessionJaafarTableId, venueJaafarTableId

SchemaUpdater = TadaBaseTableSchema()
AppHeaders = BESTrainingHeadersConfig()

def CourseSessionSchemaUpdater() -> str:
    tableId = courseSessionTableId()
    FullPath = SchemaUpdater.update_schema(tableId=tableId , AppHeaders=AppHeaders , FileName="CourseSession")
    return FullPath

def CourseSessionJaafarSchemaUpdater() -> str:
    tableId = courseSessionJaafarTableId()
    FullPath = SchemaUpdater.update_schema(tableId=tableId , AppHeaders=AppHeaders , FileName="CourseSessionJaafar")
    return FullPath

def VenueJaafarSchemaUpdater() -> str:
    tableId = venueJaafarTableId()
    FullPath = SchemaUpdater.update_schema(tableId=tableId , AppHeaders=AppHeaders , FileName="VenueJaafar")
    return FullPath



CourseSessionSchemaUpdater()
CourseSessionJaafarSchemaUpdater()
VenueJaafarSchemaUpdater()