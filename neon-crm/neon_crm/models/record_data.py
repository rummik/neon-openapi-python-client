from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordData")


@_attrs_define
class RecordData:
    """
    Attributes:
        name (Union[Unset, str]):
        value (Union[Unset, str]):
        date_format (Union[Unset, str]):
        option_values (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    date_format: Union[Unset, str] = UNSET
    option_values: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        date_format = self.date_format

        option_values = self.option_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if option_values is not UNSET:
            field_dict["optionValues"] = option_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        date_format = d.pop("dateFormat", UNSET)

        option_values = d.pop("optionValues", UNSET)

        record_data = cls(
            name=name,
            value=value,
            date_format=date_format,
            option_values=option_values,
        )

        record_data.additional_properties = d
        return record_data

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
