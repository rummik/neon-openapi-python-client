import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Timestamps")


@_attrs_define
class Timestamps:
    """
    Attributes:
        created_by (Union[Unset, str]):
        created_date_time (Union[Unset, datetime.datetime]):
        last_modified_by (Union[Unset, str]):
        last_modified_date_time (Union[Unset, datetime.datetime]):
    """

    created_by: Union[Unset, str] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    last_modified_by: Union[Unset, str] = UNSET
    last_modified_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        last_modified_by = self.last_modified_by

        last_modified_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_date_time, Unset):
            last_modified_date_time = self.last_modified_date_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_date_time is not UNSET:
            field_dict["lastModifiedDateTime"] = last_modified_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_by = d.pop("createdBy", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        last_modified_by = d.pop("lastModifiedBy", UNSET)

        _last_modified_date_time = d.pop("lastModifiedDateTime", UNSET)
        last_modified_date_time: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_date_time, Unset):
            last_modified_date_time = UNSET
        else:
            last_modified_date_time = isoparse(_last_modified_date_time)

        timestamps = cls(
            created_by=created_by,
            created_date_time=created_date_time,
            last_modified_by=last_modified_by,
            last_modified_date_time=last_modified_date_time,
        )

        timestamps.additional_properties = d
        return timestamps

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
