from enum import Enum


class TicketsPerRegistrationOperator(str, Enum):
    EXACTLY = "Exactly"
    UP_TO = "Up_to"

    def __str__(self) -> str:
        return str(self.value)
