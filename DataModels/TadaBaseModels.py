from .GeneralModels import Venue, Session
from pydantic import BaseModel


class Venue(Venue):
    wheelChairAccess: str


class Session(Session):
    attendanceTaken: str
    deleted: str
    venue: str


class Field(BaseModel):
    slug: str
    name: str
    type: str
    class Config:
        fields = {
            'type__': 'type'
        }


class insertResponse(BaseModel):
    type: str
    msg: str
    recordId: str


class SessionResponse(BaseModel):
    session: Session
    TadaBaseResponse: insertResponse

    class Config:
        copy_on_model_validation = 'none'


class VenueResponse(BaseModel):
    venue: Venue
    TadaBaseResponse: insertResponse

    class Config:
        copy_on_model_validation = 'none'






