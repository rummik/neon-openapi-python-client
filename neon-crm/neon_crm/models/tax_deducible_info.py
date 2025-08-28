from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxDeducibleInfo")


@_attrs_define
class TaxDeducibleInfo:
    """
    Attributes:
        non_deductible_amount (Union[Unset, float]):
        tax_deducible_amount (Union[Unset, float]):
        non_deductible_description (Union[Unset, str]):
    """

    non_deductible_amount: Union[Unset, float] = UNSET
    tax_deducible_amount: Union[Unset, float] = UNSET
    non_deductible_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        non_deductible_amount = self.non_deductible_amount

        tax_deducible_amount = self.tax_deducible_amount

        non_deductible_description = self.non_deductible_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if non_deductible_amount is not UNSET:
            field_dict["nonDeductibleAmount"] = non_deductible_amount
        if tax_deducible_amount is not UNSET:
            field_dict["taxDeducibleAmount"] = tax_deducible_amount
        if non_deductible_description is not UNSET:
            field_dict["nonDeductibleDescription"] = non_deductible_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        non_deductible_amount = d.pop("nonDeductibleAmount", UNSET)

        tax_deducible_amount = d.pop("taxDeducibleAmount", UNSET)

        non_deductible_description = d.pop("nonDeductibleDescription", UNSET)

        tax_deducible_info = cls(
            non_deductible_amount=non_deductible_amount,
            tax_deducible_amount=tax_deducible_amount,
            non_deductible_description=non_deductible_description,
        )

        tax_deducible_info.additional_properties = d
        return tax_deducible_info

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
