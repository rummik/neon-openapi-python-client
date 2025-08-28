import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomObjectLayoutPageItem")


@_attrs_define
class CustomObjectLayoutPageItem:
    """
    Attributes:
        layout_id (Union[Unset, int]):
        layout_name (Union[Unset, str]):
        last_modified_date_time (Union[Unset, datetime.datetime]):
        last_modified_by (Union[Unset, str]):
        is_default (Union[Unset, bool]):
    """

    layout_id: Union[Unset, int] = UNSET
    layout_name: Union[Unset, str] = UNSET
    last_modified_date_time: Union[Unset, datetime.datetime] = UNSET
    last_modified_by: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout_id = self.layout_id

        layout_name = self.layout_name

        last_modified_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_date_time, Unset):
            last_modified_date_time = self.last_modified_date_time.isoformat()

        last_modified_by = self.last_modified_by

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout_id is not UNSET:
            field_dict["layoutId"] = layout_id
        if layout_name is not UNSET:
            field_dict["layoutName"] = layout_name
        if last_modified_date_time is not UNSET:
            field_dict["lastModifiedDateTime"] = last_modified_date_time
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layout_id = d.pop("layoutId", UNSET)

        layout_name = d.pop("layoutName", UNSET)

        _last_modified_date_time = d.pop("lastModifiedDateTime", UNSET)
        last_modified_date_time: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_date_time, Unset):
            last_modified_date_time = UNSET
        else:
            last_modified_date_time = isoparse(_last_modified_date_time)

        last_modified_by = d.pop("lastModifiedBy", UNSET)

        is_default = d.pop("isDefault", UNSET)

        custom_object_layout_page_item = cls(
            layout_id=layout_id,
            layout_name=layout_name,
            last_modified_date_time=last_modified_date_time,
            last_modified_by=last_modified_by,
            is_default=is_default,
        )

        custom_object_layout_page_item.additional_properties = d
        return custom_object_layout_page_item

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
