from enum import Enum


class MembershipResponseStatus(str, Enum):
    CANCELED = "CANCELED"
    CANCEL_PENDING = "CANCEL_PENDING"
    DEFERRED = "DEFERRED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    REFUNDED = "REFUNDED"
    SUCCEEDED = "SUCCEEDED"
    WAITINGLIST = "WAITINGLIST"

    def __str__(self) -> str:
        return str(self.value)
