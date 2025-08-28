from enum import Enum


class TimeSheetApiStatus(str, Enum):
    APPROVED = "Approved"
    PENDING = "Pending"
    STILLWORKING = "StillWorking"

    def __str__(self) -> str:
        return str(self.value)
