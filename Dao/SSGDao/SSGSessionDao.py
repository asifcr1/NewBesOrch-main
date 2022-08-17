from requests.models import Response
import requests
import json

from SSGBaseDao import SSGSessionBaseDao
from APIsMaker.SSGAPIs.APISchema import RetrieveCourseSessionsSchema
from DataModels.SSGModels import Session


class SSGSessionDao(SSGSessionBaseDao):

    def _loadBytesToDict(self, courseSessionsResponse: Response) -> dict:
        courseSessionsResponseBytes = courseSessionsResponse.content
        courseSessionsResponseJson  = courseSessionsResponseBytes.decode('utf8').replace("'", '"')
        courseSessionsResponseDict  = json.loads(courseSessionsResponseJson)
        return courseSessionsResponseDict

    def _extractSessionsFromResponse(self, courseSessionsResponseDict: dict ) -> [dict]:
        courseSessions = courseSessionsResponseDict['data']['sessions']
        return courseSessions

    def retrieve(self, course_run_id: str) -> [Session]:
        APIEndPoint = RetrieveCourseSessionsSchema(course_run_id)
        courseSessionsResponse = requests.get(APIEndPoint)
        courseSessionsResponseDict = self._loadBytesToDict(courseSessionsResponse)
        courseSessions = self._extractSessionsFromResponse(courseSessionsResponseDict)
        courseSessionsObjects = [Session.parse_obj(x) for x in courseSessions]
        return courseSessionsObjects
