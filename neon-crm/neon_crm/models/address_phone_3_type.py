from enum import Enum


class AddressPhone3Type(str, Enum):
    HOME = "Home"
    MOBILE = "Mobile"
    OTHER = "Other"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
