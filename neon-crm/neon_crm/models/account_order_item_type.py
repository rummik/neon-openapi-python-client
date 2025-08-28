from enum import Enum


class AccountOrderItemType(str, Enum):
    DONATION = "DONATION"
    EVENT_REGISTRATION = "EVENT_REGISTRATION"
    MEMBERSHIP = "MEMBERSHIP"
    PRODUCT = "PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
