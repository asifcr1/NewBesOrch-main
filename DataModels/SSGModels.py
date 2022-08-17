from .GeneralModels import Session, Venue

class Venue(Venue):
    wheelChairAccess: bool


class Session(Session):
    venue: Venue
    attendanceTaken: bool
    deleted: bool
