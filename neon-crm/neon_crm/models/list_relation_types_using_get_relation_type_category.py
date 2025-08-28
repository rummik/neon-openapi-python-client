from enum import Enum


class ListRelationTypesUsingGETRelationTypeCategory(str, Enum):
    INDIVIDUAL_INDIVIDUAL = "INDIVIDUAL_INDIVIDUAL"

    def __str__(self) -> str:
        return str(self.value)
