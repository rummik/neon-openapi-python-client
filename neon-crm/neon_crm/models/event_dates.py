import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="EventDates")


@_attrs_define
class EventDates:
    """
    Attributes:
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        registration_open_date (Union[Unset, datetime.datetime]):
        registration_close_date (Union[Unset, datetime.datetime]):
        time_zone (Union[Unset, IdNamePair]):
    """

    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    registration_open_date: Union[Unset, datetime.datetime] = UNSET
    registration_close_date: Union[Unset, datetime.datetime] = UNSET
    time_zone: Union[Unset, "IdNamePair"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_time = self.start_time

        end_time = self.end_time

        registration_open_date: Union[Unset, str] = UNSET
        if not isinstance(self.registration_open_date, Unset):
            registration_open_date = self.registration_open_date.isoformat()

        registration_close_date: Union[Unset, str] = UNSET
        if not isinstance(self.registration_close_date, Unset):
            registration_close_date = self.registration_close_date.isoformat()

        time_zone: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if registration_open_date is not UNSET:
            field_dict["registrationOpenDate"] = registration_open_date
        if registration_close_date is not UNSET:
            field_dict["registrationCloseDate"] = registration_close_date
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        _registration_open_date = d.pop("registrationOpenDate", UNSET)
        registration_open_date: Union[Unset, datetime.datetime]
        if isinstance(_registration_open_date, Unset):
            registration_open_date = UNSET
        else:
            registration_open_date = isoparse(_registration_open_date)

        _registration_close_date = d.pop("registrationCloseDate", UNSET)
        registration_close_date: Union[Unset, datetime.datetime]
        if isinstance(_registration_close_date, Unset):
            registration_close_date = UNSET
        else:
            registration_close_date = isoparse(_registration_close_date)

        _time_zone = d.pop("timeZone", UNSET)
        time_zone: Union[Unset, IdNamePair]
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = IdNamePair.from_dict(_time_zone)

        event_dates = cls(
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            registration_open_date=registration_open_date,
            registration_close_date=registration_close_date,
            time_zone=time_zone,
        )

        event_dates.additional_properties = d
        return event_dates

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
