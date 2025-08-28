from enum import Enum


class CustomFieldDataComponent(str, Enum):
    ACCOUNT = "Account"
    ACTIVITY = "Activity"
    ATTENDEE = "Attendee"
    COMPANY = "Company"
    DONATION = "Donation"
    EVENT = "Event"
    GRANT = "Grant"
    INDIVIDUAL = "Individual"
    MEMBERSHIP = "Membership"
    PRODUCT = "Product"
    PROSPECT = "Prospect"

    def __str__(self) -> str:
        return str(self.value)
