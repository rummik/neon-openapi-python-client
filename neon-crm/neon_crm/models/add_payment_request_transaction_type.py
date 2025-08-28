from enum import Enum


class AddPaymentRequestTransactionType(str, Enum):
    DONATION = "DONATION"
    EVENT_REGISTRATION = "EVENT_REGISTRATION"
    MEMBERSHIP = "MEMBERSHIP"
    ORDER = "ORDER"

    def __str__(self) -> str:
        return str(self.value)
