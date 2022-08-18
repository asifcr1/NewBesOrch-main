from pydantic import BaseModel

class Venue(BaseModel):
    block: str
    street: str
    floor: str
    unit: str
    building: str
    postalCode: str
    room: str
    wheelChairAccess: bool


class Session(BaseModel):
    id: str
    startDate: str
    endDate: str
    startTime: str
    endTime: str
    modeOfTraining: str
    attendanceTaken: bool
    deleted: bool