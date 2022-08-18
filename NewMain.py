from fastapi import FastAPI
from DataModels.SSGModels import SSGSessionResponse
from Dao.SSGDao.SSGSessionDao import SSGSessionDao
from Mappers.SSGToRedisMapper import SSGToRedisMapper
from Dao.RedisDao.RedisSessionDao import RedisSessionDao, RedisJsonSessions



app = FastAPI()

@app.get("/beso/courses/runs/{runId}/sessions", response_model=RedisJsonSessions)
async def get_redis_sessions(runId: str):
    RSD = RedisSessionDao()
    CourseSessionsRedis = RSD.retrieveMember(runId)
    return CourseSessionsRedis

@app.get("/SSG/courses/runs/{runId}/sessions", response_model=SSGSessionResponse)
async def get_ssg_data(runId: str):
    SSD = SSGSessionDao()
    CourseSessionsSSG = SSD.retrieve(course_run_id=runId)
    return CourseSessionsSSG

@app.post("/beso/courses/runs/sessions/add", response_model=SSGSessionResponse)
async def insert_ssg_to_redis(sessions: SSGSessionResponse):
    SRM  = SSGToRedisMapper()
    RedisJsonSessionsObject = SRM.DataModelSessionsMapper(sessions)
    RSD = RedisSessionDao()
    RSD.addMember(RedisJsonSessionsObject)
    return sessions









