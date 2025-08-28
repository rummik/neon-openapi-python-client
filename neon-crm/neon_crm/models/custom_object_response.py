from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="CustomObjectResponse")


@_attrs_define
class CustomObjectResponse:
    """
    Attributes:
        object_id (Union[Unset, int]):
        object_name (Union[Unset, str]):
        object_label (Union[Unset, str]):
        object_description (Union[Unset, str]):
        object_api_name (Union[Unset, str]):
        object_record_name (Union[Unset, str]):
        object_record_data_type (Union[Unset, str]):
        object_record_data_length (Union[Unset, int]):
        object_record_starting_number (Union[Unset, str]):
        object_record_display_format (Union[Unset, str]):
        add_to_navigation (Union[Unset, bool]):
        allow_activity (Union[Unset, bool]):
        allow_report (Union[Unset, bool]):
        is_active (Union[Unset, bool]):
        create_webhook (Union[Unset, str]):
        update_webhook (Union[Unset, str]):
        delete_webhook (Union[Unset, str]):
        timestamps (Union[Unset, Timestamps]):
    """

    object_id: Union[Unset, int] = UNSET
    object_name: Union[Unset, str] = UNSET
    object_label: Union[Unset, str] = UNSET
    object_description: Union[Unset, str] = UNSET
    object_api_name: Union[Unset, str] = UNSET
    object_record_name: Union[Unset, str] = UNSET
    object_record_data_type: Union[Unset, str] = UNSET
    object_record_data_length: Union[Unset, int] = UNSET
    object_record_starting_number: Union[Unset, str] = UNSET
    object_record_display_format: Union[Unset, str] = UNSET
    add_to_navigation: Union[Unset, bool] = UNSET
    allow_activity: Union[Unset, bool] = UNSET
    allow_report: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    create_webhook: Union[Unset, str] = UNSET
    update_webhook: Union[Unset, str] = UNSET
    delete_webhook: Union[Unset, str] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        object_name = self.object_name

        object_label = self.object_label

        object_description = self.object_description

        object_api_name = self.object_api_name

        object_record_name = self.object_record_name

        object_record_data_type = self.object_record_data_type

        object_record_data_length = self.object_record_data_length

        object_record_starting_number = self.object_record_starting_number

        object_record_display_format = self.object_record_display_format

        add_to_navigation = self.add_to_navigation

        allow_activity = self.allow_activity

        allow_report = self.allow_report

        is_active = self.is_active

        create_webhook = self.create_webhook

        update_webhook = self.update_webhook

        delete_webhook = self.delete_webhook

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_label is not UNSET:
            field_dict["objectLabel"] = object_label
        if object_description is not UNSET:
            field_dict["objectDescription"] = object_description
        if object_api_name is not UNSET:
            field_dict["objectApiName"] = object_api_name
        if object_record_name is not UNSET:
            field_dict["objectRecordName"] = object_record_name
        if object_record_data_type is not UNSET:
            field_dict["objectRecordDataType"] = object_record_data_type
        if object_record_data_length is not UNSET:
            field_dict["objectRecordDataLength"] = object_record_data_length
        if object_record_starting_number is not UNSET:
            field_dict["objectRecordStartingNumber"] = object_record_starting_number
        if object_record_display_format is not UNSET:
            field_dict["objectRecordDisplayFormat"] = object_record_display_format
        if add_to_navigation is not UNSET:
            field_dict["addToNavigation"] = add_to_navigation
        if allow_activity is not UNSET:
            field_dict["allowActivity"] = allow_activity
        if allow_report is not UNSET:
            field_dict["allowReport"] = allow_report
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if create_webhook is not UNSET:
            field_dict["createWebhook"] = create_webhook
        if update_webhook is not UNSET:
            field_dict["updateWebhook"] = update_webhook
        if delete_webhook is not UNSET:
            field_dict["deleteWebhook"] = delete_webhook
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        object_id = d.pop("objectId", UNSET)

        object_name = d.pop("objectName", UNSET)

        object_label = d.pop("objectLabel", UNSET)

        object_description = d.pop("objectDescription", UNSET)

        object_api_name = d.pop("objectApiName", UNSET)

        object_record_name = d.pop("objectRecordName", UNSET)

        object_record_data_type = d.pop("objectRecordDataType", UNSET)

        object_record_data_length = d.pop("objectRecordDataLength", UNSET)

        object_record_starting_number = d.pop("objectRecordStartingNumber", UNSET)

        object_record_display_format = d.pop("objectRecordDisplayFormat", UNSET)

        add_to_navigation = d.pop("addToNavigation", UNSET)

        allow_activity = d.pop("allowActivity", UNSET)

        allow_report = d.pop("allowReport", UNSET)

        is_active = d.pop("isActive", UNSET)

        create_webhook = d.pop("createWebhook", UNSET)

        update_webhook = d.pop("updateWebhook", UNSET)

        delete_webhook = d.pop("deleteWebhook", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        custom_object_response = cls(
            object_id=object_id,
            object_name=object_name,
            object_label=object_label,
            object_description=object_description,
            object_api_name=object_api_name,
            object_record_name=object_record_name,
            object_record_data_type=object_record_data_type,
            object_record_data_length=object_record_data_length,
            object_record_starting_number=object_record_starting_number,
            object_record_display_format=object_record_display_format,
            add_to_navigation=add_to_navigation,
            allow_activity=allow_activity,
            allow_report=allow_report,
            is_active=is_active,
            create_webhook=create_webhook,
            update_webhook=update_webhook,
            delete_webhook=delete_webhook,
            timestamps=timestamps,
        )

        custom_object_response.additional_properties = d
        return custom_object_response

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
