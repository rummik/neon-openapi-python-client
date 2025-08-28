from enum import Enum


class CustomObjectFieldListResponseFieldDataType(str, Enum):
    AUTO_NUMBER = "AUTO_NUMBER"
    CHECKBOX = "CHECKBOX"
    CHECKBOX_SINGLE = "CHECKBOX_SINGLE"
    DATE = "DATE"
    DATETIME = "DATETIME"
    DROPDOWN = "DROPDOWN"
    EMAIL = "EMAIL"
    FILE = "FILE"
    FORMULA = "FORMULA"
    LOOKUP = "LOOKUP"
    MASTER_DETAIL = "MASTER_DETAIL"
    NUMBER = "NUMBER"
    PERCENT = "PERCENT"
    PHONE = "PHONE"
    RADIO = "RADIO"
    TEXT = "TEXT"
    TEXTAREA = "TEXTAREA"
    TEXTAREA_SHORT = "TEXTAREA_SHORT"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
