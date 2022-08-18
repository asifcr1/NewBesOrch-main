from pydantic import BaseModel
from .GeneralModels import Session, Venue
from typing import List


class SSGVenue(Venue):
    pass


class SSGSession(Session):
    venue: SSGVenue

class SSGSessionResponse(BaseModel):
    runID: str
    sessions: List[SSGSession]


