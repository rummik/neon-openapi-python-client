from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_trigger import WebhookTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_basic import HttpBasic
    from ..models.name_value_pair import NameValuePair


T = TypeVar("T", bound="Webhook")


@_attrs_define
class Webhook:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        url (Union[Unset, str]):
        trigger (Union[Unset, WebhookTrigger]):
        content_type (Union[Unset, str]):
        trigger_self_import (Union[Unset, bool]):
        http_basic (Union[Unset, HttpBasic]):
        custom_parameters (Union[Unset, list['NameValuePair']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    trigger: Union[Unset, WebhookTrigger] = UNSET
    content_type: Union[Unset, str] = UNSET
    trigger_self_import: Union[Unset, bool] = UNSET
    http_basic: Union[Unset, "HttpBasic"] = UNSET
    custom_parameters: Union[Unset, list["NameValuePair"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        content_type = self.content_type

        trigger_self_import = self.trigger_self_import

        http_basic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_basic, Unset):
            http_basic = self.http_basic.to_dict()

        custom_parameters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_parameters, Unset):
            custom_parameters = []
            for custom_parameters_item_data in self.custom_parameters:
                custom_parameters_item = custom_parameters_item_data.to_dict()
                custom_parameters.append(custom_parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if trigger_self_import is not UNSET:
            field_dict["triggerSelfImport"] = trigger_self_import
        if http_basic is not UNSET:
            field_dict["httpBasic"] = http_basic
        if custom_parameters is not UNSET:
            field_dict["customParameters"] = custom_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_basic import HttpBasic
        from ..models.name_value_pair import NameValuePair

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, WebhookTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = WebhookTrigger(_trigger)

        content_type = d.pop("contentType", UNSET)

        trigger_self_import = d.pop("triggerSelfImport", UNSET)

        _http_basic = d.pop("httpBasic", UNSET)
        http_basic: Union[Unset, HttpBasic]
        if isinstance(_http_basic, Unset):
            http_basic = UNSET
        else:
            http_basic = HttpBasic.from_dict(_http_basic)

        custom_parameters = []
        _custom_parameters = d.pop("customParameters", UNSET)
        for custom_parameters_item_data in _custom_parameters or []:
            custom_parameters_item = NameValuePair.from_dict(custom_parameters_item_data)

            custom_parameters.append(custom_parameters_item)

        webhook = cls(
            id=id,
            name=name,
            url=url,
            trigger=trigger,
            content_type=content_type,
            trigger_self_import=trigger_self_import,
            http_basic=http_basic,
            custom_parameters=custom_parameters,
        )

        webhook.additional_properties = d
        return webhook

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
