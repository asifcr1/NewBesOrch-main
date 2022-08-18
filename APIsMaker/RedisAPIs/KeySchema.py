
def HashedIDsTadaBaseSchema(tableName: str) -> str:
    return "tadabase:idstovalues:" + tableName

def CourseSessionJsonKeySchema(runId: str) -> str:
    return "courserun:" + runId + ":coursesessions"