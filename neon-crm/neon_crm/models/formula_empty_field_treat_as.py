from enum import Enum


class FormulaEmptyFieldTreatAs(str, Enum):
    BLANK = "BLANK"
    ZEROS = "ZEROS"

    def __str__(self) -> str:
        return str(self.value)
