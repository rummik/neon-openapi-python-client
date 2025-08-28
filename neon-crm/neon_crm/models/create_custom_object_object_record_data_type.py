from enum import Enum


class CreateCustomObjectObjectRecordDataType(str, Enum):
    AUTO_NUMBER = "AUTO_NUMBER"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
