from enum import Enum


class DonationStatus(str, Enum):
    CANCELED = "Canceled"
    DEFERRED = "Deferred"
    FAILED = "Failed"
    PENDING = "Pending"
    REFUNDED = "Refunded"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
