from enum import Enum


class ECheckPaymentAccountType(str, Enum):
    CHECKING = "Checking"
    SAVING = "Saving"

    def __str__(self) -> str:
        return str(self.value)
