from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CraInfo")


@_attrs_define
class CraInfo:
    """
    Attributes:
        advantage_amount (Union[Unset, float]):
        eligible_amount (Union[Unset, float]):
        advantage_description (Union[Unset, str]):
    """

    advantage_amount: Union[Unset, float] = UNSET
    eligible_amount: Union[Unset, float] = UNSET
    advantage_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advantage_amount = self.advantage_amount

        eligible_amount = self.eligible_amount

        advantage_description = self.advantage_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advantage_amount is not UNSET:
            field_dict["advantageAmount"] = advantage_amount
        if eligible_amount is not UNSET:
            field_dict["eligibleAmount"] = eligible_amount
        if advantage_description is not UNSET:
            field_dict["advantageDescription"] = advantage_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advantage_amount = d.pop("advantageAmount", UNSET)

        eligible_amount = d.pop("eligibleAmount", UNSET)

        advantage_description = d.pop("advantageDescription", UNSET)

        cra_info = cls(
            advantage_amount=advantage_amount,
            eligible_amount=eligible_amount,
            advantage_description=advantage_description,
        )

        cra_info.additional_properties = d
        return cra_info

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
