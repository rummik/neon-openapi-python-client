from enum import Enum


class CustomObjectEmailNotificationNotificationType(str, Enum):
    API = "API"
    BACK_END = "BACK_END"
    FRONT_END = "FRONT_END"

    def __str__(self) -> str:
        return str(self.value)
