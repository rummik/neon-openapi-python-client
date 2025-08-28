from enum import Enum


class CheckPaymentAccountType(str, Enum):
    CHECKING = "Checking"
    SAVING = "Saving"

    def __str__(self) -> str:
        return str(self.value)
