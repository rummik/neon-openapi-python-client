from enum import Enum


class FormulaReturnDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATETIME = "DATETIME"
    NUMBER = "NUMBER"
    PERCENT = "PERCENT"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
