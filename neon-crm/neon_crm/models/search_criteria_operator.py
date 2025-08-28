from enum import Enum


class SearchCriteriaOperator(str, Enum):
    BLANK = "BLANK"
    CONTAIN = "CONTAIN"
    EQUAL = "EQUAL"
    GREATER_AND_EQUAL = "GREATER_AND_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    IN_RANGE = "IN_RANGE"
    LESS_AND_EQUAL = "LESS_AND_EQUAL"
    LESS_THAN = "LESS_THAN"
    NOT_BLANK = "NOT_BLANK"
    NOT_CONTAIN = "NOT_CONTAIN"
    NOT_EQUAL = "NOT_EQUAL"
    NOT_IN_RANGE = "NOT_IN_RANGE"

    def __str__(self) -> str:
        return str(self.value)
