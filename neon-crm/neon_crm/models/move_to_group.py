from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveToGroup")


@_attrs_define
class MoveToGroup:
    """
    Attributes:
        group_id (Union[Unset, str]):
        custom_fields (Union[Unset, list[str]]):
    """

    group_id: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        custom_fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        custom_fields = cast(list[str], d.pop("customFields", UNSET))

        move_to_group = cls(
            group_id=group_id,
            custom_fields=custom_fields,
        )

        move_to_group.additional_properties = d
        return move_to_group

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
