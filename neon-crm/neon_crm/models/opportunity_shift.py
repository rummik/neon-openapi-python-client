import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="OpportunityShift")


@_attrs_define
class OpportunityShift:
    """
    Attributes:
        name (str):
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        id (Union[Unset, str]):
        occurrence_id (Union[Unset, str]):
        ng_occurrence_id (Union[Unset, str]):
        description (Union[Unset, str]):
        timezone_id (Union[Unset, int]):
        max_volunteer (Union[Unset, int]):
        location_name (Union[Unset, str]):
        sync_location (Union[Unset, bool]):
        address (Union[Unset, Address]):
        timestamps (Union[Unset, Timestamps]):
    """

    name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    id: Union[Unset, str] = UNSET
    occurrence_id: Union[Unset, str] = UNSET
    ng_occurrence_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    max_volunteer: Union[Unset, int] = UNSET
    location_name: Union[Unset, str] = UNSET
    sync_location: Union[Unset, bool] = UNSET
    address: Union[Unset, "Address"] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        id = self.id

        occurrence_id = self.occurrence_id

        ng_occurrence_id = self.ng_occurrence_id

        description = self.description

        timezone_id = self.timezone_id

        max_volunteer = self.max_volunteer

        location_name = self.location_name

        sync_location = self.sync_location

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if occurrence_id is not UNSET:
            field_dict["occurrenceId"] = occurrence_id
        if ng_occurrence_id is not UNSET:
            field_dict["ngOccurrenceId"] = ng_occurrence_id
        if description is not UNSET:
            field_dict["description"] = description
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if max_volunteer is not UNSET:
            field_dict["maxVolunteer"] = max_volunteer
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if sync_location is not UNSET:
            field_dict["syncLocation"] = sync_location
        if address is not UNSET:
            field_dict["address"] = address
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        name = d.pop("name")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        id = d.pop("id", UNSET)

        occurrence_id = d.pop("occurrenceId", UNSET)

        ng_occurrence_id = d.pop("ngOccurrenceId", UNSET)

        description = d.pop("description", UNSET)

        timezone_id = d.pop("timezoneId", UNSET)

        max_volunteer = d.pop("maxVolunteer", UNSET)

        location_name = d.pop("locationName", UNSET)

        sync_location = d.pop("syncLocation", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        opportunity_shift = cls(
            name=name,
            start_date=start_date,
            end_date=end_date,
            id=id,
            occurrence_id=occurrence_id,
            ng_occurrence_id=ng_occurrence_id,
            description=description,
            timezone_id=timezone_id,
            max_volunteer=max_volunteer,
            location_name=location_name,
            sync_location=sync_location,
            address=address,
            timestamps=timestamps,
        )

        opportunity_shift.additional_properties = d
        return opportunity_shift

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
