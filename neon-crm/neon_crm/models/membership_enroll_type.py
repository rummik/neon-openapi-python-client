from enum import Enum


class MembershipEnrollType(str, Enum):
    JOIN = "JOIN"
    REJOIN = "REJOIN"
    RENEW = "RENEW"

    def __str__(self) -> str:
        return str(self.value)
