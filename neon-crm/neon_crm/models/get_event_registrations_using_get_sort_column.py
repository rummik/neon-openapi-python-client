from enum import Enum


class GetEventRegistrationsUsingGETSortColumn(str, Enum):
    REGISTRATIONDATETIME = "registrationDateTime"

    def __str__(self) -> str:
        return str(self.value)
