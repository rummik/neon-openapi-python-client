from enum import Enum


class ListMembershipUsingGETSortColumn(str, Enum):
    AMOUNT = "amount"
    DATE = "date"

    def __str__(self) -> str:
        return str(self.value)
