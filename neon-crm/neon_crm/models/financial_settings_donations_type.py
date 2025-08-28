from enum import Enum


class FinancialSettingsDonationsType(str, Enum):
    FREEINPUT = "FreeInput"
    LEVEL = "LEVEL"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
