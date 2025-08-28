from enum import Enum


class MasterDetailDeleteAction(str, Enum):
    BLOCK = "BLOCK"
    CASCADE = "CASCADE"

    def __str__(self) -> str:
        return str(self.value)
