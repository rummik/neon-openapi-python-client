import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.event_attendee_phone_1_type import EventAttendeePhone1Type
from ..models.event_attendee_registration_status import EventAttendeeRegistrationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField
    from ..models.dob import Dob


T = TypeVar("T", bound="EventAttendee")


@_attrs_define
class EventAttendee:
    """
    Attributes:
        attendee_id (Union[Unset, int]):
        account_id (Union[Unset, str]):
        prefix (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        marked_attended (Union[Unset, bool]):
        attendee_custom_fields (Union[Unset, list['CustomField']]):
        registrant_account_id (Union[Unset, str]):
        registration_status (Union[Unset, EventAttendeeRegistrationStatus]):
        registration_date (Union[Unset, datetime.datetime]):
        email (Union[Unset, str]):
        company_name (Union[Unset, str]):
        address_line_1 (Union[Unset, str]):
        city (Union[Unset, str]):
        state_province (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        phone1 (Union[Unset, str]):
        phone_1_type (Union[Unset, EventAttendeePhone1Type]):
        dob (Union[Unset, Dob]):
        event_name (Union[Unset, str]):
        registration_id (Union[Unset, str]):
        ticket_name (Union[Unset, str]):
    """

    attendee_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    marked_attended: Union[Unset, bool] = UNSET
    attendee_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    registrant_account_id: Union[Unset, str] = UNSET
    registration_status: Union[Unset, EventAttendeeRegistrationStatus] = UNSET
    registration_date: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_province: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    phone1: Union[Unset, str] = UNSET
    phone_1_type: Union[Unset, EventAttendeePhone1Type] = UNSET
    dob: Union[Unset, "Dob"] = UNSET
    event_name: Union[Unset, str] = UNSET
    registration_id: Union[Unset, str] = UNSET
    ticket_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attendee_id = self.attendee_id

        account_id = self.account_id

        prefix = self.prefix

        first_name = self.first_name

        last_name = self.last_name

        marked_attended = self.marked_attended

        attendee_custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attendee_custom_fields, Unset):
            attendee_custom_fields = []
            for attendee_custom_fields_item_data in self.attendee_custom_fields:
                attendee_custom_fields_item = attendee_custom_fields_item_data.to_dict()
                attendee_custom_fields.append(attendee_custom_fields_item)

        registrant_account_id = self.registrant_account_id

        registration_status: Union[Unset, str] = UNSET
        if not isinstance(self.registration_status, Unset):
            registration_status = self.registration_status.value

        registration_date: Union[Unset, str] = UNSET
        if not isinstance(self.registration_date, Unset):
            registration_date = self.registration_date.isoformat()

        email = self.email

        company_name = self.company_name

        address_line_1 = self.address_line_1

        city = self.city

        state_province = self.state_province

        zip_code = self.zip_code

        phone1 = self.phone1

        phone_1_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_1_type, Unset):
            phone_1_type = self.phone_1_type.value

        dob: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dob, Unset):
            dob = self.dob.to_dict()

        event_name = self.event_name

        registration_id = self.registration_id

        ticket_name = self.ticket_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attendee_id is not UNSET:
            field_dict["attendeeId"] = attendee_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if marked_attended is not UNSET:
            field_dict["markedAttended"] = marked_attended
        if attendee_custom_fields is not UNSET:
            field_dict["attendeeCustomFields"] = attendee_custom_fields
        if registrant_account_id is not UNSET:
            field_dict["registrantAccountId"] = registrant_account_id
        if registration_status is not UNSET:
            field_dict["registrationStatus"] = registration_status
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if email is not UNSET:
            field_dict["email"] = email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["stateProvince"] = state_province
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if phone1 is not UNSET:
            field_dict["phone1"] = phone1
        if phone_1_type is not UNSET:
            field_dict["phone1Type"] = phone_1_type
        if dob is not UNSET:
            field_dict["dob"] = dob
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if registration_id is not UNSET:
            field_dict["registrationId"] = registration_id
        if ticket_name is not UNSET:
            field_dict["ticketName"] = ticket_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field import CustomField
        from ..models.dob import Dob

        d = dict(src_dict)
        attendee_id = d.pop("attendeeId", UNSET)

        account_id = d.pop("accountId", UNSET)

        prefix = d.pop("prefix", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        marked_attended = d.pop("markedAttended", UNSET)

        attendee_custom_fields = []
        _attendee_custom_fields = d.pop("attendeeCustomFields", UNSET)
        for attendee_custom_fields_item_data in _attendee_custom_fields or []:
            attendee_custom_fields_item = CustomField.from_dict(attendee_custom_fields_item_data)

            attendee_custom_fields.append(attendee_custom_fields_item)

        registrant_account_id = d.pop("registrantAccountId", UNSET)

        _registration_status = d.pop("registrationStatus", UNSET)
        registration_status: Union[Unset, EventAttendeeRegistrationStatus]
        if isinstance(_registration_status, Unset):
            registration_status = UNSET
        else:
            registration_status = EventAttendeeRegistrationStatus(_registration_status)

        _registration_date = d.pop("registrationDate", UNSET)
        registration_date: Union[Unset, datetime.datetime]
        if isinstance(_registration_date, Unset):
            registration_date = UNSET
        else:
            registration_date = isoparse(_registration_date)

        email = d.pop("email", UNSET)

        company_name = d.pop("companyName", UNSET)

        address_line_1 = d.pop("addressLine1", UNSET)

        city = d.pop("city", UNSET)

        state_province = d.pop("stateProvince", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        phone1 = d.pop("phone1", UNSET)

        _phone_1_type = d.pop("phone1Type", UNSET)
        phone_1_type: Union[Unset, EventAttendeePhone1Type]
        if isinstance(_phone_1_type, Unset):
            phone_1_type = UNSET
        else:
            phone_1_type = EventAttendeePhone1Type(_phone_1_type)

        _dob = d.pop("dob", UNSET)
        dob: Union[Unset, Dob]
        if isinstance(_dob, Unset):
            dob = UNSET
        else:
            dob = Dob.from_dict(_dob)

        event_name = d.pop("eventName", UNSET)

        registration_id = d.pop("registrationId", UNSET)

        ticket_name = d.pop("ticketName", UNSET)

        event_attendee = cls(
            attendee_id=attendee_id,
            account_id=account_id,
            prefix=prefix,
            first_name=first_name,
            last_name=last_name,
            marked_attended=marked_attended,
            attendee_custom_fields=attendee_custom_fields,
            registrant_account_id=registrant_account_id,
            registration_status=registration_status,
            registration_date=registration_date,
            email=email,
            company_name=company_name,
            address_line_1=address_line_1,
            city=city,
            state_province=state_province,
            zip_code=zip_code,
            phone1=phone1,
            phone_1_type=phone_1_type,
            dob=dob,
            event_name=event_name,
            registration_id=registration_id,
            ticket_name=ticket_name,
        )

        event_attendee.additional_properties = d
        return event_attendee

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
