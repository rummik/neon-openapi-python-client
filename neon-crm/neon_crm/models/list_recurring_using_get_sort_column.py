from enum import Enum


class ListRecurringUsingGETSortColumn(str, Enum):
    AMOUNT = "amount"
    ENDDATE = "endDate"
    FIRSTNAME = "firstName"
    LASTNAME = "lastName"
    NEXTPAYMENTDATE = "nextPaymentDate"

    def __str__(self) -> str:
        return str(self.value)
