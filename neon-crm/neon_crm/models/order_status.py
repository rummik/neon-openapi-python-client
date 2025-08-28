from enum import Enum


class OrderStatus(str, Enum):
    CANCELED = "Canceled"
    DEFERRED = "Deferred"
    DISPUTE_LOST = "Dispute_Lost"
    ERROR = "Error"
    FAILED = "Failed"
    HELD_FOR_REVIEW = "Held_for_Review"
    PARTIALLY_REFUNDED = "Partially_Refunded"
    PENDING = "Pending"
    PROCESSING = "Processing"
    REFUNDED = "Refunded"
    SCHEDULED = "Scheduled"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
