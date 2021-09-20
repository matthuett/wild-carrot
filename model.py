import datetime as dt
from enum import Enum


class Festival:
    """
    Recurring event
    """
    def __init__(self, name: str, start: dt.date, end: dt.date):
        self.name = name
        self.start = start
        self.end = end

    @property
    def duration(self) -> dt.timedelta:
        return self.end - self.start


class TicketType(Enum):
    EARLYBIRD = {"name": "earlybird", "price": 100}
    NORMAL = {"name": "normal", "price": 150}
    STAFF = {"name": "staff", "price": 0}


class Account:
    pass


class Ticket:
    """
    Festival ticket purchased before entry of the festival. The ticket gets assigned to an account.
    """
    def __init__(self, festival: Festival, ticket_type: TicketType):
        self.festival = festival
        self._type = ticket_type

    @property
    def ticket_type(self) -> TicketType:
        return self._type

    @ticket_type.setter
    def ticket_type(self, value: TicketType) -> None:
        if not isinstance(value, TicketType):
            raise ValueError("Only assignment of TicketType objects possible.")
        self._type = value