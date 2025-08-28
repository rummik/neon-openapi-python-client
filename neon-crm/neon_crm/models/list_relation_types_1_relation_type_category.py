from enum import Enum


class ListRelationTypes1RelationTypeCategory(str, Enum):
    INDIVIDUAL_INDIVIDUAL = "INDIVIDUAL_INDIVIDUAL"

    def __str__(self) -> str:
        return str(self.value)
