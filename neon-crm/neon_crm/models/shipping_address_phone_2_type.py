from enum import Enum


class ShippingAddressPhone2Type(str, Enum):
    HOME = "Home"
    MOBILE = "Mobile"
    OTHER = "Other"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
