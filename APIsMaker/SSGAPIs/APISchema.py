main_entry = "https://mock-api.ssg-wsg.sg/"

def RetrieveCourseSessionsSchema(runId: str) -> str:
    api = main_entry + f'courses/runs/{runId}/sessions'
    return api

