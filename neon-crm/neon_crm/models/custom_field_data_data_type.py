from enum import Enum


class CustomFieldDataDataType(str, Enum):
    AMOUNT = "Amount"
    AREA_CODE = "Area_Code"
    BOOLEAN = "Boolean"
    CURRENCY = "Currency"
    DATE = "Date"
    DECIMAL = "Decimal"
    EMAIL = "Email"
    FLOAT = "Float"
    INTEGER = "Integer"
    NAME = "Name"
    PHONE = "Phone"
    TEXT = "Text"
    TIME = "Time"
    WHOLE_NUMBER = "Whole_Number"

    def __str__(self) -> str:
        return str(self.value)
