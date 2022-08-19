from fastapi import FastAPI
from Routers import Sessions

app = FastAPI()
app.include_router(Sessions.router)
