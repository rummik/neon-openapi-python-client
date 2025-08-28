from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Number")


@_attrs_define
class Number:
    """
    Attributes:
        default_value (Union[Unset, str]):
        is_required (Union[Unset, bool]):
        length (Union[Unset, int]):
        decimal_length (Union[Unset, int]):
        is_unique (Union[Unset, bool]):
        display_format (Union[Unset, str]):
    """

    default_value: Union[Unset, str] = UNSET
    is_required: Union[Unset, bool] = UNSET
    length: Union[Unset, int] = UNSET
    decimal_length: Union[Unset, int] = UNSET
    is_unique: Union[Unset, bool] = UNSET
    display_format: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_value = self.default_value

        is_required = self.is_required

        length = self.length

        decimal_length = self.decimal_length

        is_unique = self.is_unique

        display_format = self.display_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if length is not UNSET:
            field_dict["length"] = length
        if decimal_length is not UNSET:
            field_dict["decimalLength"] = decimal_length
        if is_unique is not UNSET:
            field_dict["isUnique"] = is_unique
        if display_format is not UNSET:
            field_dict["displayFormat"] = display_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_value = d.pop("defaultValue", UNSET)

        is_required = d.pop("isRequired", UNSET)

        length = d.pop("length", UNSET)

        decimal_length = d.pop("decimalLength", UNSET)

        is_unique = d.pop("isUnique", UNSET)

        display_format = d.pop("displayFormat", UNSET)

        number = cls(
            default_value=default_value,
            is_required=is_required,
            length=length,
            decimal_length=decimal_length,
            is_unique=is_unique,
            display_format=display_format,
        )

        number.additional_properties = d
        return number

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
