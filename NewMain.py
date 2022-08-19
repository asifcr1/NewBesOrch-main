from fastapi import FastAPI
from Routers import Sessions

description = """
BESOrchestrator is a group of well-organized and well-managed APIs to help moving Data between different data sources 
and achieve the data centralization across all different apps!

## Courses

You will be having the following APIs:

* **Retrieve courses details from SSG API** (_not implemented_).


## Course Runs

You will be having the following APIs:

* **Synchronize courses runs across all data sources** (_not implemented_).


## Course Sessions

You will be having the following APIs:

* **Retrieve course sessions from SSG API** (_implemented_).
* **Retrieve course sessions from TadaBase API** (_implemented_).
* **Insert course sessions to be stored in our centralized data storage in BESOrchestrator** (_implemented_).
* **Retrieve course sessions from our centralized data storage in BESOrchestrator** (_implemented_).
* **Insert course sessions through BESOrchestrator to SSG** (_not implemented_).
* **Insert course sessions through BESOrchestrator to TadaBase** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "Sessions",
        "description": "Holds the operations of course Sessions. It will take care of CRUD and Synchronizing operations\
         for course Sessions"
    },
]

app = FastAPI(
    title="BESOrchestrator API",
    description=description,
    version="1.0.0 Beta",
    openapi_tags=tags_metadata
)
app.include_router(Sessions.router)
