from enum import Enum


class ListRecurringUsingGETStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
