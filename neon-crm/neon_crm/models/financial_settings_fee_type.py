from enum import Enum


class FinancialSettingsFeeType(str, Enum):
    FREE = "Free"
    MT_MA = "MT_MA"
    MT_OA = "MT_OA"
    SINGLEFEE = "SingleFee"

    def __str__(self) -> str:
        return str(self.value)
