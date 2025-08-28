from enum import Enum


class GetEventRegistrationsUsingGET1SortField(str, Enum):
    REGISTRATIONDATETIME = "registrationDateTime"

    def __str__(self) -> str:
        return str(self.value)
