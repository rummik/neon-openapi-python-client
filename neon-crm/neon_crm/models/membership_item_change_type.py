from enum import Enum


class MembershipItemChangeType(str, Enum):
    DOWNGRADED = "DOWNGRADED"
    UNCHANGED = "UNCHANGED"
    UPGRADED = "UPGRADED"

    def __str__(self) -> str:
        return str(self.value)
