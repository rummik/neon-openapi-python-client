from enum import Enum


class TributeType(str, Enum):
    HONOR = "Honor"
    MEMORY = "Memory"

    def __str__(self) -> str:
        return str(self.value)
