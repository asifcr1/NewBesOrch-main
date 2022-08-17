from pydantic import BaseModel
from typing import Union
from .TadaBaseModels import SessionResponse, VenueResponse

class TadaBaseSessionModelResponse(BaseModel):
    sessionResponse: SessionResponse
    venueResponse: Union[VenueResponse, dict]

