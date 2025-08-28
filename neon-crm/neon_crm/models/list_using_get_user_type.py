from enum import Enum


class ListUsingGETUserType(str, Enum):
    COMPANY = "COMPANY"
    INDIVIDUAL = "INDIVIDUAL"

    def __str__(self) -> str:
        return str(self.value)
