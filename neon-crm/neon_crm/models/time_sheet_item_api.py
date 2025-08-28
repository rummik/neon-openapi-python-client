import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="TimeSheetItemApi")


@_attrs_define
class TimeSheetItemApi:
    """
    Attributes:
        id (Union[Unset, str]):
        time_sheet_id (Union[Unset, str]):
        shift_id (Union[Unset, str]):
        role_id (Union[Unset, str]):
        date (Union[Unset, datetime.date]):
        hours (Union[Unset, float]):
        expenses (Union[Unset, float]):
        mileages (Union[Unset, float]):
        timestamps (Union[Unset, Timestamps]):
    """

    id: Union[Unset, str] = UNSET
    time_sheet_id: Union[Unset, str] = UNSET
    shift_id: Union[Unset, str] = UNSET
    role_id: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    hours: Union[Unset, float] = UNSET
    expenses: Union[Unset, float] = UNSET
    mileages: Union[Unset, float] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        time_sheet_id = self.time_sheet_id

        shift_id = self.shift_id

        role_id = self.role_id

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        hours = self.hours

        expenses = self.expenses

        mileages = self.mileages

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time_sheet_id is not UNSET:
            field_dict["timeSheetId"] = time_sheet_id
        if shift_id is not UNSET:
            field_dict["shiftId"] = shift_id
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if date is not UNSET:
            field_dict["date"] = date
        if hours is not UNSET:
            field_dict["hours"] = hours
        if expenses is not UNSET:
            field_dict["expenses"] = expenses
        if mileages is not UNSET:
            field_dict["mileages"] = mileages
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        time_sheet_id = d.pop("timeSheetId", UNSET)

        shift_id = d.pop("shiftId", UNSET)

        role_id = d.pop("roleId", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        hours = d.pop("hours", UNSET)

        expenses = d.pop("expenses", UNSET)

        mileages = d.pop("mileages", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        time_sheet_item_api = cls(
            id=id,
            time_sheet_id=time_sheet_id,
            shift_id=shift_id,
            role_id=role_id,
            date=date,
            hours=hours,
            expenses=expenses,
            mileages=mileages,
            timestamps=timestamps,
        )

        time_sheet_item_api.additional_properties = d
        return time_sheet_item_api

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
