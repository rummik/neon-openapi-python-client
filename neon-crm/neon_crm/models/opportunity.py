import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.opportunity_status import OpportunityStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.id_name_pair import IdNamePair
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="Opportunity")


@_attrs_define
class Opportunity:
    """
    Attributes:
        name (str):
        start_date (datetime.datetime):
        end_date (datetime.datetime):
        id (Union[Unset, str]):
        sys_user_account_id (Union[Unset, str]):
        contact_id (Union[Unset, str]):
        event_id (Union[Unset, str]):
        ng_event_id (Union[Unset, str]):
        categories (Union[Unset, list['IdNamePair']]):
        description (Union[Unset, str]):
        max_volunteers (Union[Unset, int]):
        mileage_enabled (Union[Unset, bool]):
        expenses_enabled (Union[Unset, bool]):
        shift_enabled (Union[Unset, bool]):
        status (Union[Unset, OpportunityStatus]):
        available_online (Union[Unset, bool]):
        location_name (Union[Unset, str]):
        address (Union[Unset, Address]):
        timestamps (Union[Unset, Timestamps]):
    """

    name: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    id: Union[Unset, str] = UNSET
    sys_user_account_id: Union[Unset, str] = UNSET
    contact_id: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    ng_event_id: Union[Unset, str] = UNSET
    categories: Union[Unset, list["IdNamePair"]] = UNSET
    description: Union[Unset, str] = UNSET
    max_volunteers: Union[Unset, int] = UNSET
    mileage_enabled: Union[Unset, bool] = UNSET
    expenses_enabled: Union[Unset, bool] = UNSET
    shift_enabled: Union[Unset, bool] = UNSET
    status: Union[Unset, OpportunityStatus] = UNSET
    available_online: Union[Unset, bool] = UNSET
    location_name: Union[Unset, str] = UNSET
    address: Union[Unset, "Address"] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        id = self.id

        sys_user_account_id = self.sys_user_account_id

        contact_id = self.contact_id

        event_id = self.event_id

        ng_event_id = self.ng_event_id

        categories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        description = self.description

        max_volunteers = self.max_volunteers

        mileage_enabled = self.mileage_enabled

        expenses_enabled = self.expenses_enabled

        shift_enabled = self.shift_enabled

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        available_online = self.available_online

        location_name = self.location_name

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
        if sys_user_account_id is not UNSET:
            field_dict["sysUserAccountId"] = sys_user_account_id
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if ng_event_id is not UNSET:
            field_dict["ngEventId"] = ng_event_id
        if categories is not UNSET:
            field_dict["categories"] = categories
        if description is not UNSET:
            field_dict["description"] = description
        if max_volunteers is not UNSET:
            field_dict["maxVolunteers"] = max_volunteers
        if mileage_enabled is not UNSET:
            field_dict["mileageEnabled"] = mileage_enabled
        if expenses_enabled is not UNSET:
            field_dict["expensesEnabled"] = expenses_enabled
        if shift_enabled is not UNSET:
            field_dict["shiftEnabled"] = shift_enabled
        if status is not UNSET:
            field_dict["status"] = status
        if available_online is not UNSET:
            field_dict["availableOnline"] = available_online
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if address is not UNSET:
            field_dict["address"] = address
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.id_name_pair import IdNamePair
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        name = d.pop("name")

        start_date = isoparse(d.pop("startDate"))

        end_date = isoparse(d.pop("endDate"))

        id = d.pop("id", UNSET)

        sys_user_account_id = d.pop("sysUserAccountId", UNSET)

        contact_id = d.pop("contactId", UNSET)

        event_id = d.pop("eventId", UNSET)

        ng_event_id = d.pop("ngEventId", UNSET)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = IdNamePair.from_dict(categories_item_data)

            categories.append(categories_item)

        description = d.pop("description", UNSET)

        max_volunteers = d.pop("maxVolunteers", UNSET)

        mileage_enabled = d.pop("mileageEnabled", UNSET)

        expenses_enabled = d.pop("expensesEnabled", UNSET)

        shift_enabled = d.pop("shiftEnabled", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OpportunityStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OpportunityStatus(_status)

        available_online = d.pop("availableOnline", UNSET)

        location_name = d.pop("locationName", UNSET)

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

        opportunity = cls(
            name=name,
            start_date=start_date,
            end_date=end_date,
            id=id,
            sys_user_account_id=sys_user_account_id,
            contact_id=contact_id,
            event_id=event_id,
            ng_event_id=ng_event_id,
            categories=categories,
            description=description,
            max_volunteers=max_volunteers,
            mileage_enabled=mileage_enabled,
            expenses_enabled=expenses_enabled,
            shift_enabled=shift_enabled,
            status=status,
            available_online=available_online,
            location_name=location_name,
            address=address,
            timestamps=timestamps,
        )

        opportunity.additional_properties = d
        return opportunity

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
