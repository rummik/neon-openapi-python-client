from enum import Enum


class BaseMembershipChangeType(str, Enum):
    DOWNGRADED = "DOWNGRADED"
    UNCHANGED = "UNCHANGED"
    UPGRADED = "UPGRADED"

    def __str__(self) -> str:
        return str(self.value)
