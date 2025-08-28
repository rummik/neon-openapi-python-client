from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldOptionValue")


@_attrs_define
class FieldOptionValue:
    """
    Attributes:
        option_id (Union[Unset, int]):
        option_value (Union[Unset, str]):
        sequence (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        is_default (Union[Unset, bool]):
    """

    option_id: Union[Unset, int] = UNSET
    option_value: Union[Unset, str] = UNSET
    sequence: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_id = self.option_id

        option_value = self.option_value

        sequence = self.sequence

        is_active = self.is_active

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_id is not UNSET:
            field_dict["optionId"] = option_id
        if option_value is not UNSET:
            field_dict["optionValue"] = option_value
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option_id = d.pop("optionId", UNSET)

        option_value = d.pop("optionValue", UNSET)

        sequence = d.pop("sequence", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_default = d.pop("isDefault", UNSET)

        field_option_value = cls(
            option_id=option_id,
            option_value=option_value,
            sequence=sequence,
            is_active=is_active,
            is_default=is_default,
        )

        field_option_value.additional_properties = d
        return field_option_value

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
