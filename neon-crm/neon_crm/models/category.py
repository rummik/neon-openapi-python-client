from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category_status import CategoryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """
    Attributes:
        code (Union[Unset, str]):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        display_sequence (Union[Unset, int]):
        status (Union[Unset, CategoryStatus]):
    """

    code: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_sequence: Union[Unset, int] = UNSET
    status: Union[Unset, CategoryStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        id = self.id

        description = self.description

        name = self.name

        display_sequence = self.display_sequence

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if display_sequence is not UNSET:
            field_dict["displaySequence"] = display_sequence
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        display_sequence = d.pop("displaySequence", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CategoryStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CategoryStatus(_status)

        category = cls(
            code=code,
            id=id,
            description=description,
            name=name,
            display_sequence=display_sequence,
            status=status,
        )

        category.additional_properties = d
        return category

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
