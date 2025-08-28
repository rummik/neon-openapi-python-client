import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSearchResultItem")


@_attrs_define
class EventSearchResultItem:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        code (Union[Unset, str]):
        capacity (Union[Unset, int]):
        archived (Union[Unset, bool]):
        description (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        start_time (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, str]):
        publish_event (Union[Unset, bool]):
        enable_event_registration_form (Union[Unset, bool]):
        address_line_1 (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        address_line_3 (Union[Unset, str]):
        address_line_4 (Union[Unset, str]):
        address_type (Union[Unset, str]):
        address_city (Union[Unset, str]):
        address_zip_code (Union[Unset, str]):
        address_zip_code_suffix (Union[Unset, str]):
        address_country (Union[Unset, str]):
        campaign_code (Union[Unset, str]):
        campaign_name (Union[Unset, str]):
        fund_code (Union[Unset, str]):
        fund_name (Union[Unset, str]):
        purpose_code (Union[Unset, str]):
        purpose_name (Union[Unset, str]):
        thumbnail_url (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    capacity: Union[Unset, int] = UNSET
    archived: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, str] = UNSET
    publish_event: Union[Unset, bool] = UNSET
    enable_event_registration_form: Union[Unset, bool] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    address_line_4: Union[Unset, str] = UNSET
    address_type: Union[Unset, str] = UNSET
    address_city: Union[Unset, str] = UNSET
    address_zip_code: Union[Unset, str] = UNSET
    address_zip_code_suffix: Union[Unset, str] = UNSET
    address_country: Union[Unset, str] = UNSET
    campaign_code: Union[Unset, str] = UNSET
    campaign_name: Union[Unset, str] = UNSET
    fund_code: Union[Unset, str] = UNSET
    fund_name: Union[Unset, str] = UNSET
    purpose_code: Union[Unset, str] = UNSET
    purpose_name: Union[Unset, str] = UNSET
    thumbnail_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        code = self.code

        capacity = self.capacity

        archived = self.archived

        description = self.description

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_time = self.start_time

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        end_time = self.end_time

        publish_event = self.publish_event

        enable_event_registration_form = self.enable_event_registration_form

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        address_line_3 = self.address_line_3

        address_line_4 = self.address_line_4

        address_type = self.address_type

        address_city = self.address_city

        address_zip_code = self.address_zip_code

        address_zip_code_suffix = self.address_zip_code_suffix

        address_country = self.address_country

        campaign_code = self.campaign_code

        campaign_name = self.campaign_name

        fund_code = self.fund_code

        fund_name = self.fund_name

        purpose_code = self.purpose_code

        purpose_name = self.purpose_name

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if archived is not UNSET:
            field_dict["archived"] = archived
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if publish_event is not UNSET:
            field_dict["publishEvent"] = publish_event
        if enable_event_registration_form is not UNSET:
            field_dict["enableEventRegistrationForm"] = enable_event_registration_form
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if address_line_4 is not UNSET:
            field_dict["addressLine4"] = address_line_4
        if address_type is not UNSET:
            field_dict["addressType"] = address_type
        if address_city is not UNSET:
            field_dict["addressCity"] = address_city
        if address_zip_code is not UNSET:
            field_dict["addressZipCode"] = address_zip_code
        if address_zip_code_suffix is not UNSET:
            field_dict["addressZipCodeSuffix"] = address_zip_code_suffix
        if address_country is not UNSET:
            field_dict["addressCountry"] = address_country
        if campaign_code is not UNSET:
            field_dict["campaignCode"] = campaign_code
        if campaign_name is not UNSET:
            field_dict["campaignName"] = campaign_name
        if fund_code is not UNSET:
            field_dict["fundCode"] = fund_code
        if fund_name is not UNSET:
            field_dict["fundName"] = fund_name
        if purpose_code is not UNSET:
            field_dict["purposeCode"] = purpose_code
        if purpose_name is not UNSET:
            field_dict["purposeName"] = purpose_name
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        capacity = d.pop("capacity", UNSET)

        archived = d.pop("archived", UNSET)

        description = d.pop("description", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        start_time = d.pop("startTime", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        end_time = d.pop("endTime", UNSET)

        publish_event = d.pop("publishEvent", UNSET)

        enable_event_registration_form = d.pop("enableEventRegistrationForm", UNSET)

        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        address_line_4 = d.pop("addressLine4", UNSET)

        address_type = d.pop("addressType", UNSET)

        address_city = d.pop("addressCity", UNSET)

        address_zip_code = d.pop("addressZipCode", UNSET)

        address_zip_code_suffix = d.pop("addressZipCodeSuffix", UNSET)

        address_country = d.pop("addressCountry", UNSET)

        campaign_code = d.pop("campaignCode", UNSET)

        campaign_name = d.pop("campaignName", UNSET)

        fund_code = d.pop("fundCode", UNSET)

        fund_name = d.pop("fundName", UNSET)

        purpose_code = d.pop("purposeCode", UNSET)

        purpose_name = d.pop("purposeName", UNSET)

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        event_search_result_item = cls(
            id=id,
            name=name,
            code=code,
            capacity=capacity,
            archived=archived,
            description=description,
            start_date=start_date,
            start_time=start_time,
            end_date=end_date,
            end_time=end_time,
            publish_event=publish_event,
            enable_event_registration_form=enable_event_registration_form,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
            address_line_4=address_line_4,
            address_type=address_type,
            address_city=address_city,
            address_zip_code=address_zip_code,
            address_zip_code_suffix=address_zip_code_suffix,
            address_country=address_country,
            campaign_code=campaign_code,
            campaign_name=campaign_name,
            fund_code=fund_code,
            fund_name=fund_name,
            purpose_code=purpose_code,
            purpose_name=purpose_name,
            thumbnail_url=thumbnail_url,
        )

        event_search_result_item.additional_properties = d
        return event_search_result_item

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
