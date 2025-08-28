from enum import Enum


class AccountCustomFieldDataAccountType(str, Enum):
    ANY = "Any"
    COMPANY = "Company"
    INDIVIDUAL = "Individual"

    def __str__(self) -> str:
        return str(self.value)
