from enum import Enum


class MembershipLevelType(str, Enum):
    COMPANY = "COMPANY"
    HOUSEHOLD = "HOUSEHOLD"
    NO_GROUP = "NO_GROUP"

    def __str__(self) -> str:
        return str(self.value)
