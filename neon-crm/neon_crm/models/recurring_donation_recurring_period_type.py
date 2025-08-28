from enum import Enum


class RecurringDonationRecurringPeriodType(str, Enum):
    DAY = "DAY"
    LIFE = "LIFE"
    MONTH = "MONTH"
    WEEK = "WEEK"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
