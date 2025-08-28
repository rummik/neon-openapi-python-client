from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_object_email_notification_notification_type import CustomObjectEmailNotificationNotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomObjectEmailNotification")


@_attrs_define
class CustomObjectEmailNotification:
    """
    Attributes:
        notification_type (Union[Unset, CustomObjectEmailNotificationNotificationType]):
        enable (Union[Unset, bool]):
    """

    notification_type: Union[Unset, CustomObjectEmailNotificationNotificationType] = UNSET
    enable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_type is not UNSET:
            field_dict["notificationType"] = notification_type
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _notification_type = d.pop("notificationType", UNSET)
        notification_type: Union[Unset, CustomObjectEmailNotificationNotificationType]
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = CustomObjectEmailNotificationNotificationType(_notification_type)

        enable = d.pop("enable", UNSET)

        custom_object_email_notification = cls(
            notification_type=notification_type,
            enable=enable,
        )

        custom_object_email_notification.additional_properties = d
        return custom_object_email_notification

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
