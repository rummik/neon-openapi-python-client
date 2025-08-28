from enum import Enum


class DonationAnonymousType(str, Enum):
    DONATIONAMOUNTANONYMOUS = "DonationAmountAnonymous"
    DONORNAMEANONYMOUS = "DonorNameAnonymous"
    NO = "No"

    def __str__(self) -> str:
        return str(self.value)
