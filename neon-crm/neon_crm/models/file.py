from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """
    Attributes:
        is_required (Union[Unset, bool]):
        max_file_size (Union[Unset, int]):
        allow_file_types (Union[Unset, str]):
        available_to_public (Union[Unset, bool]):
    """

    is_required: Union[Unset, bool] = UNSET
    max_file_size: Union[Unset, int] = UNSET
    allow_file_types: Union[Unset, str] = UNSET
    available_to_public: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_required = self.is_required

        max_file_size = self.max_file_size

        allow_file_types = self.allow_file_types

        available_to_public = self.available_to_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if max_file_size is not UNSET:
            field_dict["maxFileSize"] = max_file_size
        if allow_file_types is not UNSET:
            field_dict["allowFileTypes"] = allow_file_types
        if available_to_public is not UNSET:
            field_dict["availableToPublic"] = available_to_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_required = d.pop("isRequired", UNSET)

        max_file_size = d.pop("maxFileSize", UNSET)

        allow_file_types = d.pop("allowFileTypes", UNSET)

        available_to_public = d.pop("availableToPublic", UNSET)

        file = cls(
            is_required=is_required,
            max_file_size=max_file_size,
            allow_file_types=allow_file_types,
            available_to_public=available_to_public,
        )

        file.additional_properties = d
        return file

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
