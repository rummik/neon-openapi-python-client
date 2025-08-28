from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoNumber")


@_attrs_define
class AutoNumber:
    """
    Attributes:
        starting_number (Union[Unset, int]):
        display_format (Union[Unset, str]):
    """

    starting_number: Union[Unset, int] = UNSET
    display_format: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starting_number = self.starting_number

        display_format = self.display_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if starting_number is not UNSET:
            field_dict["startingNumber"] = starting_number
        if display_format is not UNSET:
            field_dict["displayFormat"] = display_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starting_number = d.pop("startingNumber", UNSET)

        display_format = d.pop("displayFormat", UNSET)

        auto_number = cls(
            starting_number=starting_number,
            display_format=display_format,
        )

        auto_number.additional_properties = d
        return auto_number

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
