from enum import Enum


class MembershipTermUnit(str, Enum):
    DAY = "DAY"
    LIFE = "LIFE"
    MONTH = "MONTH"
    WEEKLY = "WEEKLY"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
