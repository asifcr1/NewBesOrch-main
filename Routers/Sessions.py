from fastapi import APIRouter
from DataModels.SSGModels import SSGSessionResponse
from Dao.SSGDao.SSGSessionDao import SSGSessionDao
from Mappers.SSGToRedisMapper import SSGToRedisMapper
from Dao.RedisDao.RedisSessionDao import RedisSessionDao, RedisJsonSessions



router = APIRouter()


@router.get("/beso/courses/runs/{runId}/sessions", response_model=RedisJsonSessions, tags=['Sessions'])
async def get_redis_sessions(runId: str):
    RSD = RedisSessionDao()
    CourseSessionsRedis = RSD.retrieveMember(runId)
    return CourseSessionsRedis

@router.get("/SSG/courses/runs/{runId}/sessions", response_model=SSGSessionResponse, tags=['Sessions'])
async def get_ssg_data(runId: str):
    SSD = SSGSessionDao()
    CourseSessionsSSG = SSD.retrieve(course_run_id=runId)
    return CourseSessionsSSG

@router.post("/beso/courses/runs/sessions/add", response_model=SSGSessionResponse, tags=['Sessions'])
async def insert_ssg_to_redis(sessions: SSGSessionResponse):
    SRM  = SSGToRedisMapper()
    RedisJsonSessionsObject = SRM.DataModelSessionsMapper(sessions)
    RSD = RedisSessionDao()
    RSD.addMember(RedisJsonSessionsObject)
    return sessions









