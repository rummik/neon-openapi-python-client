from enum import Enum


class MembershipLevelScopeType(str, Enum):
    ALL_CONTACTS = "ALL_CONTACTS"
    CURRENT_EMPLOYEES = "CURRENT_EMPLOYEES"

    def __str__(self) -> str:
        return str(self.value)
