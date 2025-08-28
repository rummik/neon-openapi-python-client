from enum import Enum


class VolunteerRoleApiStatusColor(str, Enum):
    BLUE = "Blue"
    GREEN = "Green"
    GREY = "Grey"
    ORANGE = "Orange"
    PLACEHOLDER = "Placeholder"
    PURPLE = "Purple"
    RED = "Red"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
