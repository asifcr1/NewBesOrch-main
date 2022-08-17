from pydantic import BaseModel


class SessionIDTadaBase(BaseModel):
    sessionId: str
    TadaBaseRecordId : str


class VenueIDTadaBase(BaseModel):
    venueObject: str
    TadaBaseRecordId : str