from enum import Enum


class MembershipTermType(str, Enum):
    JOIN = "JOIN"
    RENEW = "RENEW"

    def __str__(self) -> str:
        return str(self.value)
