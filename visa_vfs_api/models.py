from dataclasses import dataclass
from enum import Enum


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
