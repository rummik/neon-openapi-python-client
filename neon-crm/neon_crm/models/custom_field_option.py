from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldOption")


@_attrs_define
class CustomFieldOption:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        visible_on_public_forms (Union[Unset, bool]):
        visible_on_constituent_forms (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    visible_on_public_forms: Union[Unset, bool] = UNSET
    visible_on_constituent_forms: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        visible_on_public_forms = self.visible_on_public_forms

        visible_on_constituent_forms = self.visible_on_constituent_forms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if visible_on_public_forms is not UNSET:
            field_dict["visibleOnPublicForms"] = visible_on_public_forms
        if visible_on_constituent_forms is not UNSET:
            field_dict["visibleOnConstituentForms"] = visible_on_constituent_forms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        visible_on_public_forms = d.pop("visibleOnPublicForms", UNSET)

        visible_on_constituent_forms = d.pop("visibleOnConstituentForms", UNSET)

        custom_field_option = cls(
            id=id,
            name=name,
            visible_on_public_forms=visible_on_public_forms,
            visible_on_constituent_forms=visible_on_constituent_forms,
        )

        custom_field_option.additional_properties = d
        return custom_field_option

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
