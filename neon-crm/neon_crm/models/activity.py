from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_priority import ActivityPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_dates import ActivityDates
    from ..models.id_name_pair import IdNamePair
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """
    Attributes:
        subject (str):
        activity_dates (ActivityDates):
        status (IdNamePair):
        priority (ActivityPriority):
        id (Union[Unset, str]):
        note (Union[Unset, str]):
        client_id (Union[Unset, str]):
        system_user_id (Union[Unset, str]):
        grant_id (Union[Unset, str]):
        timestamps (Union[Unset, Timestamps]):
    """

    subject: str
    activity_dates: "ActivityDates"
    status: "IdNamePair"
    priority: ActivityPriority
    id: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    system_user_id: Union[Unset, str] = UNSET
    grant_id: Union[Unset, str] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        activity_dates = self.activity_dates.to_dict()

        status = self.status.to_dict()

        priority = self.priority.value

        id = self.id

        note = self.note

        client_id = self.client_id

        system_user_id = self.system_user_id

        grant_id = self.grant_id

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "activityDates": activity_dates,
                "status": status,
                "priority": priority,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if system_user_id is not UNSET:
            field_dict["systemUserId"] = system_user_id
        if grant_id is not UNSET:
            field_dict["grantId"] = grant_id
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_dates import ActivityDates
        from ..models.id_name_pair import IdNamePair
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        subject = d.pop("subject")

        activity_dates = ActivityDates.from_dict(d.pop("activityDates"))

        status = IdNamePair.from_dict(d.pop("status"))

        priority = ActivityPriority(d.pop("priority"))

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        client_id = d.pop("clientId", UNSET)

        system_user_id = d.pop("systemUserId", UNSET)

        grant_id = d.pop("grantId", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        activity = cls(
            subject=subject,
            activity_dates=activity_dates,
            status=status,
            priority=priority,
            id=id,
            note=note,
            client_id=client_id,
            system_user_id=system_user_id,
            grant_id=grant_id,
            timestamps=timestamps,
        )

        activity.additional_properties = d
        return activity

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
