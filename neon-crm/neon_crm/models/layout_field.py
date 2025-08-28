from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LayoutField")


@_attrs_define
class LayoutField:
    """
    Attributes:
        object_api_name (Union[Unset, str]):
        field_api_name (Union[Unset, str]):
    """

    object_api_name: Union[Unset, str] = UNSET
    field_api_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_api_name = self.object_api_name

        field_api_name = self.field_api_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_api_name is not UNSET:
            field_dict["objectApiName"] = object_api_name
        if field_api_name is not UNSET:
            field_dict["fieldApiName"] = field_api_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_api_name = d.pop("objectApiName", UNSET)

        field_api_name = d.pop("fieldApiName", UNSET)

        layout_field = cls(
            object_api_name=object_api_name,
            field_api_name=field_api_name,
        )

        layout_field.additional_properties = d
        return layout_field

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
