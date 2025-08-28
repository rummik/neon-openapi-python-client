import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="ActivityDates")


@_attrs_define
class ActivityDates:
    """
    Attributes:
        start_date (datetime.datetime):
        time_zone (IdNamePair):
        end_date (Union[Unset, datetime.datetime]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
    """

    start_date: datetime.datetime
    time_zone: "IdNamePair"
    end_date: Union[Unset, datetime.datetime] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        time_zone = self.time_zone.to_dict()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startDate": start_date,
                "timeZone": time_zone,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        start_date = isoparse(d.pop("startDate"))

        time_zone = IdNamePair.from_dict(d.pop("timeZone"))

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        activity_dates = cls(
            start_date=start_date,
            time_zone=time_zone,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
        )

        activity_dates.additional_properties = d
        return activity_dates

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
