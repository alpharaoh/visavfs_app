from enum import Enum
from dataclasses import dataclass


class AppointmentState(Enum):
    Unavailable = "Unavailable"
    Available = "Available"


class CountryCode(Enum):
    Britain = "gbr"
    Italy = "ita"


@dataclass
class Option:
    id: int
    option: str

    @property
    def x_path(self) -> str:
        return f'//*[@id="mat-select-value-{self.id}"]'
