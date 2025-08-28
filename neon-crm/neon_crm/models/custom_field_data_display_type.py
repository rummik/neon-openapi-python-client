from enum import Enum


class CustomFieldDataDisplayType(str, Enum):
    ACCOUNT = "Account"
    CHECKBOX = "Checkbox"
    DROPDOWN = "Dropdown"
    FILE = "File"
    MULTILINETEXT = "MultiLineText"
    ONELINETEXT = "OneLineText"
    PASSWORD = "Password"
    RADIO = "Radio"

    def __str__(self) -> str:
        return str(self.value)
