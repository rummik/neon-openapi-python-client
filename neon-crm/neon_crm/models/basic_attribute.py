from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicAttribute")


@_attrs_define
class BasicAttribute:
    """
    Attributes:
        default_value (Union[Unset, str]):
        is_required (Union[Unset, bool]):
    """

    default_value: Union[Unset, str] = UNSET
    is_required: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_value = self.default_value

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_value = d.pop("defaultValue", UNSET)

        is_required = d.pop("isRequired", UNSET)

        basic_attribute = cls(
            default_value=default_value,
            is_required=is_required,
        )

        basic_attribute.additional_properties = d
        return basic_attribute

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
