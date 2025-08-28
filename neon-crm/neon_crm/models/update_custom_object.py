from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCustomObject")


@_attrs_define
class UpdateCustomObject:
    """
    Attributes:
        object_label (Union[Unset, str]):
        object_description (Union[Unset, str]):
        allow_activity (Union[Unset, bool]):
        allow_report (Union[Unset, bool]):
        add_to_navigation (Union[Unset, bool]):
        create_webhook (Union[Unset, str]):
        update_webhook (Union[Unset, str]):
        delete_webhook (Union[Unset, str]):
        is_active (Union[Unset, bool]):
    """

    object_label: Union[Unset, str] = UNSET
    object_description: Union[Unset, str] = UNSET
    allow_activity: Union[Unset, bool] = UNSET
    allow_report: Union[Unset, bool] = UNSET
    add_to_navigation: Union[Unset, bool] = UNSET
    create_webhook: Union[Unset, str] = UNSET
    update_webhook: Union[Unset, str] = UNSET
    delete_webhook: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_label = self.object_label

        object_description = self.object_description

        allow_activity = self.allow_activity

        allow_report = self.allow_report

        add_to_navigation = self.add_to_navigation

        create_webhook = self.create_webhook

        update_webhook = self.update_webhook

        delete_webhook = self.delete_webhook

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_label is not UNSET:
            field_dict["objectLabel"] = object_label
        if object_description is not UNSET:
            field_dict["objectDescription"] = object_description
        if allow_activity is not UNSET:
            field_dict["allowActivity"] = allow_activity
        if allow_report is not UNSET:
            field_dict["allowReport"] = allow_report
        if add_to_navigation is not UNSET:
            field_dict["addToNavigation"] = add_to_navigation
        if create_webhook is not UNSET:
            field_dict["createWebhook"] = create_webhook
        if update_webhook is not UNSET:
            field_dict["updateWebhook"] = update_webhook
        if delete_webhook is not UNSET:
            field_dict["deleteWebhook"] = delete_webhook
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_label = d.pop("objectLabel", UNSET)

        object_description = d.pop("objectDescription", UNSET)

        allow_activity = d.pop("allowActivity", UNSET)

        allow_report = d.pop("allowReport", UNSET)

        add_to_navigation = d.pop("addToNavigation", UNSET)

        create_webhook = d.pop("createWebhook", UNSET)

        update_webhook = d.pop("updateWebhook", UNSET)

        delete_webhook = d.pop("deleteWebhook", UNSET)

        is_active = d.pop("isActive", UNSET)

        update_custom_object = cls(
            object_label=object_label,
            object_description=object_description,
            allow_activity=allow_activity,
            allow_report=allow_report,
            add_to_navigation=add_to_navigation,
            create_webhook=create_webhook,
            update_webhook=update_webhook,
            delete_webhook=delete_webhook,
            is_active=is_active,
        )

        update_custom_object.additional_properties = d
        return update_custom_object

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
