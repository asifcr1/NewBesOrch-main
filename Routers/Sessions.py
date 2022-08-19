from fastapi import APIRouter
from DataModels.SSGModels import SSGSessionResponse
from Dao.SSGDao.SSGSessionDao import SSGSessionDao
from Mappers.SSGToRedisMapper import SSGToRedisMapper
from Dao.RedisDao.RedisSessionDao import RedisSessionDao, RedisJsonSessions



router = APIRouter()


@router.get("/beso/courses/runs/{runId}/sessions", response_model=RedisJsonSessions, tags=['Sessions'],
            summary="Retrieve course run's sessions from center storage ",
            response_description="List of sessions retrieved")
async def get_redis_sessions(runId: str):
    """
        Insert the sessions with following information:

        - **run ID**: The ID of course run that contains all the sessions
        """
    RSD = RedisSessionDao()
    CourseSessionsRedis = RSD.retrieveMember(runId)
    return CourseSessionsRedis

@router.get("/SSG/courses/runs/{runId}/sessions", response_model=SSGSessionResponse, tags=['Sessions'],
            summary="Retrieve course run's sessions from SSG API ",
            response_description="List of sessions retrieved"
            )
async def get_ssg_data(runId: str):
    """
        Insert the sessions with following information:

        - **run ID**: The ID of course run that contains all the sessions
        """
    SSD = SSGSessionDao()
    CourseSessionsSSG = SSD.retrieve(course_run_id=runId)
    return CourseSessionsSSG

@router.post("/beso/courses/runs/sessions/add", response_model=SSGSessionResponse, tags=['Sessions'],
             summary="Insert course run's sessions to the center storage ",
             response_description="List of sessions inserted"
             )
async def insert_ssg_to_redis(sessions: SSGSessionResponse):
    """
       Insert the sessions with following information:

       - **run ID**: The ID of course run that contains all the sessions
       - **Session ID**: a unique ID across sessions
       - **modeOfTraining**: Enum value to indicate the type of training of the session
       - **attendanceTaken**: A boolean value indicates whether there's an attendance checking for this session or not
       - **deleted**: A boolean value indicates whether the session was deleted later or not
       - **startDate**
       - **endDate**
       - **startTime**
       - **endTime**
       """
    SRM  = SSGToRedisMapper()
    RedisJsonSessionsObject = SRM.DataModelSessionsMapper(sessions)
    RSD = RedisSessionDao()
    RSD.addMember(RedisJsonSessionsObject)
    return sessions









