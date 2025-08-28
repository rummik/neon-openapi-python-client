from enum import Enum


class TimeSheetSearchParamStatusListItem(str, Enum):
    APPROVED = "Approved"
    PENDING = "Pending"
    STILLWORKING = "StillWorking"

    def __str__(self) -> str:
        return str(self.value)
