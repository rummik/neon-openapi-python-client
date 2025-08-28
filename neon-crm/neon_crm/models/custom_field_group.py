from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_group_component import CustomFieldGroupComponent
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldGroup")


@_attrs_define
class CustomFieldGroup:
    """
    Attributes:
        display_name (str):
        component (CustomFieldGroupComponent):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    display_name: str
    component: CustomFieldGroupComponent
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        component = self.component.value

        id = self.id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "component": component,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName")

        component = CustomFieldGroupComponent(d.pop("component"))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        custom_field_group = cls(
            display_name=display_name,
            component=component,
            id=id,
            description=description,
        )

        custom_field_group.additional_properties = d
        return custom_field_group

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
