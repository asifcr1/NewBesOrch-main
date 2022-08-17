import abc

from DataModels.TadaBaseModels import Session, Venue
from DataModels.TadaBaseModels import SessionResponse, VenueResponse


class TadaBaseSessionBaseDao(abc.ABC):
    @abc.abstractmethod
    def insert(self, session: Session) -> SessionResponse:
        pass


class TadaBaseVenueBaseDao(abc.ABC):
    @abc.abstractmethod
    def insert(self, venue: Venue) -> VenueResponse:
        pass