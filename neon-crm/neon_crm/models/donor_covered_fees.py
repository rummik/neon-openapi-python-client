from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DonorCoveredFees")


@_attrs_define
class DonorCoveredFees:
    """
    Attributes:
        credit_card_fee (Union[Unset, float]):
        credit_card_am_ex_fee (Union[Unset, float]):
        credit_card_master_card_fee (Union[Unset, float]):
        ach_fee (Union[Unset, float]):
    """

    credit_card_fee: Union[Unset, float] = UNSET
    credit_card_am_ex_fee: Union[Unset, float] = UNSET
    credit_card_master_card_fee: Union[Unset, float] = UNSET
    ach_fee: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit_card_fee = self.credit_card_fee

        credit_card_am_ex_fee = self.credit_card_am_ex_fee

        credit_card_master_card_fee = self.credit_card_master_card_fee

        ach_fee = self.ach_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_card_fee is not UNSET:
            field_dict["creditCardFee"] = credit_card_fee
        if credit_card_am_ex_fee is not UNSET:
            field_dict["creditCardAmExFee"] = credit_card_am_ex_fee
        if credit_card_master_card_fee is not UNSET:
            field_dict["creditCardMasterCardFee"] = credit_card_master_card_fee
        if ach_fee is not UNSET:
            field_dict["achFee"] = ach_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit_card_fee = d.pop("creditCardFee", UNSET)

        credit_card_am_ex_fee = d.pop("creditCardAmExFee", UNSET)

        credit_card_master_card_fee = d.pop("creditCardMasterCardFee", UNSET)

        ach_fee = d.pop("achFee", UNSET)

        donor_covered_fees = cls(
            credit_card_fee=credit_card_fee,
            credit_card_am_ex_fee=credit_card_am_ex_fee,
            credit_card_master_card_fee=credit_card_master_card_fee,
            ach_fee=ach_fee,
        )

        donor_covered_fees.additional_properties = d
        return donor_covered_fees

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
