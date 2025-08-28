import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.time_sheet_api_status import TimeSheetApiStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_sheet_item_api import TimeSheetItemApi
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="TimeSheetApi")


@_attrs_define
class TimeSheetApi:
    """
    Attributes:
        account_id (str):
        week_of (datetime.date):
        status (TimeSheetApiStatus):
        id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        time_sheet_items (Union[Unset, list['TimeSheetItemApi']]):
        total_hours (Union[Unset, float]):
        total_expenses (Union[Unset, float]):
        total_mileages (Union[Unset, float]):
        approval_datetime (Union[Unset, datetime.datetime]):
        approval_by (Union[Unset, str]):
        timestamps (Union[Unset, Timestamps]):
    """

    account_id: str
    week_of: datetime.date
    status: TimeSheetApiStatus
    id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    time_sheet_items: Union[Unset, list["TimeSheetItemApi"]] = UNSET
    total_hours: Union[Unset, float] = UNSET
    total_expenses: Union[Unset, float] = UNSET
    total_mileages: Union[Unset, float] = UNSET
    approval_datetime: Union[Unset, datetime.datetime] = UNSET
    approval_by: Union[Unset, str] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        week_of = self.week_of.isoformat()

        status = self.status.value

        id = self.id

        project_id = self.project_id

        time_sheet_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.time_sheet_items, Unset):
            time_sheet_items = []
            for time_sheet_items_item_data in self.time_sheet_items:
                time_sheet_items_item = time_sheet_items_item_data.to_dict()
                time_sheet_items.append(time_sheet_items_item)

        total_hours = self.total_hours

        total_expenses = self.total_expenses

        total_mileages = self.total_mileages

        approval_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.approval_datetime, Unset):
            approval_datetime = self.approval_datetime.isoformat()

        approval_by = self.approval_by

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "weekOf": week_of,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if time_sheet_items is not UNSET:
            field_dict["timeSheetItems"] = time_sheet_items
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours
        if total_expenses is not UNSET:
            field_dict["totalExpenses"] = total_expenses
        if total_mileages is not UNSET:
            field_dict["totalMileages"] = total_mileages
        if approval_datetime is not UNSET:
            field_dict["approvalDatetime"] = approval_datetime
        if approval_by is not UNSET:
            field_dict["approvalBy"] = approval_by
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_sheet_item_api import TimeSheetItemApi
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        account_id = d.pop("accountId")

        week_of = isoparse(d.pop("weekOf")).date()

        status = TimeSheetApiStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        project_id = d.pop("projectId", UNSET)

        time_sheet_items = []
        _time_sheet_items = d.pop("timeSheetItems", UNSET)
        for time_sheet_items_item_data in _time_sheet_items or []:
            time_sheet_items_item = TimeSheetItemApi.from_dict(time_sheet_items_item_data)

            time_sheet_items.append(time_sheet_items_item)

        total_hours = d.pop("totalHours", UNSET)

        total_expenses = d.pop("totalExpenses", UNSET)

        total_mileages = d.pop("totalMileages", UNSET)

        _approval_datetime = d.pop("approvalDatetime", UNSET)
        approval_datetime: Union[Unset, datetime.datetime]
        if isinstance(_approval_datetime, Unset):
            approval_datetime = UNSET
        else:
            approval_datetime = isoparse(_approval_datetime)

        approval_by = d.pop("approvalBy", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        time_sheet_api = cls(
            account_id=account_id,
            week_of=week_of,
            status=status,
            id=id,
            project_id=project_id,
            time_sheet_items=time_sheet_items,
            total_hours=total_hours,
            total_expenses=total_expenses,
            total_mileages=total_mileages,
            approval_datetime=approval_datetime,
            approval_by=approval_by,
            timestamps=timestamps,
        )

        time_sheet_api.additional_properties = d
        return time_sheet_api

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
