from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class CustomerRequest:
    date_init: date
    date_end: date


@dataclass
class DatastoreData:
    cnm: str
    date_request: datetime
    document: str
    ip: str
    name: str
    number: int
    url: str
    value: float
    ip_cliente: str = field(default=None)
    motivo: str = field(default=None)

    def __repr__(self):
        return f'{self.name}, documento: {self.document} do IP: {self.ip_cliente}'
