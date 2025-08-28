from enum import Enum


class ConsentSms(str, Enum):
    DECLINED = "DECLINED"
    GIVEN = "GIVEN"
    NOT_ASKED = "NOT_ASKED"

    def __str__(self) -> str:
        return str(self.value)
