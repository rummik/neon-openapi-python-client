from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.custom_field import CustomField
    from ..models.id_name_pair import IdNamePair
    from ..models.tax_deducible_info import TaxDeducibleInfo
    from ..models.ticket import Ticket


T = TypeVar("T", bound="EventRegistrationItem")


@_attrs_define
class EventRegistrationItem:
    """
    Attributes:
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
        id (Union[Unset, str]):
        event_id (Union[Unset, str]):
        registration_date_time (Union[Unset, str]):  Example: 2020-03-26 02:46:00+00:00.
        coupon_code (Union[Unset, str]):
        send_system_email (Union[Unset, bool]):
        registration_amount (Union[Unset, float]):
        ignore_capacity (Union[Unset, bool]):
        registrant_account_id (Union[Unset, str]):
        fundraiser_account_id (Union[Unset, str]):
        registrant_custom_fields (Union[Unset, list['CustomField']]):
        tickets (Union[Unset, list['Ticket']]):
        source (Union[Unset, IdNamePair]):
    """

    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    id: Union[Unset, str] = UNSET
    event_id: Union[Unset, str] = UNSET
    registration_date_time: Union[Unset, str] = UNSET
    coupon_code: Union[Unset, str] = UNSET
    send_system_email: Union[Unset, bool] = UNSET
    registration_amount: Union[Unset, float] = UNSET
    ignore_capacity: Union[Unset, bool] = UNSET
    registrant_account_id: Union[Unset, str] = UNSET
    fundraiser_account_id: Union[Unset, str] = UNSET
    registrant_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    tickets: Union[Unset, list["Ticket"]] = UNSET
    source: Union[Unset, "IdNamePair"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        id = self.id

        event_id = self.event_id

        registration_date_time = self.registration_date_time

        coupon_code = self.coupon_code

        send_system_email = self.send_system_email

        registration_amount = self.registration_amount

        ignore_capacity = self.ignore_capacity

        registrant_account_id = self.registrant_account_id

        fundraiser_account_id = self.fundraiser_account_id

        registrant_custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.registrant_custom_fields, Unset):
            registrant_custom_fields = []
            for registrant_custom_fields_item_data in self.registrant_custom_fields:
                registrant_custom_fields_item = registrant_custom_fields_item_data.to_dict()
                registrant_custom_fields.append(registrant_custom_fields_item)

        tickets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tickets, Unset):
            tickets = []
            for tickets_item_data in self.tickets:
                tickets_item = tickets_item_data.to_dict()
                tickets.append(tickets_item)

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info
        if id is not UNSET:
            field_dict["id"] = id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if registration_date_time is not UNSET:
            field_dict["registrationDateTime"] = registration_date_time
        if coupon_code is not UNSET:
            field_dict["couponCode"] = coupon_code
        if send_system_email is not UNSET:
            field_dict["sendSystemEmail"] = send_system_email
        if registration_amount is not UNSET:
            field_dict["registrationAmount"] = registration_amount
        if ignore_capacity is not UNSET:
            field_dict["ignoreCapacity"] = ignore_capacity
        if registrant_account_id is not UNSET:
            field_dict["registrantAccountId"] = registrant_account_id
        if fundraiser_account_id is not UNSET:
            field_dict["fundraiserAccountId"] = fundraiser_account_id
        if registrant_custom_fields is not UNSET:
            field_dict["registrantCustomFields"] = registrant_custom_fields
        if tickets is not UNSET:
            field_dict["tickets"] = tickets
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.custom_field import CustomField
        from ..models.id_name_pair import IdNamePair
        from ..models.tax_deducible_info import TaxDeducibleInfo
        from ..models.ticket import Ticket

        d = dict(src_dict)
        _cra_info = d.pop("craInfo", UNSET)
        cra_info: Union[Unset, CraInfo]
        if isinstance(_cra_info, Unset):
            cra_info = UNSET
        else:
            cra_info = CraInfo.from_dict(_cra_info)

        _tax_deductible_info = d.pop("taxDeductibleInfo", UNSET)
        tax_deductible_info: Union[Unset, TaxDeducibleInfo]
        if isinstance(_tax_deductible_info, Unset):
            tax_deductible_info = UNSET
        else:
            tax_deductible_info = TaxDeducibleInfo.from_dict(_tax_deductible_info)

        id = d.pop("id", UNSET)

        event_id = d.pop("eventId", UNSET)

        registration_date_time = d.pop("registrationDateTime", UNSET)

        coupon_code = d.pop("couponCode", UNSET)

        send_system_email = d.pop("sendSystemEmail", UNSET)

        registration_amount = d.pop("registrationAmount", UNSET)

        ignore_capacity = d.pop("ignoreCapacity", UNSET)

        registrant_account_id = d.pop("registrantAccountId", UNSET)

        fundraiser_account_id = d.pop("fundraiserAccountId", UNSET)

        registrant_custom_fields = []
        _registrant_custom_fields = d.pop("registrantCustomFields", UNSET)
        for registrant_custom_fields_item_data in _registrant_custom_fields or []:
            registrant_custom_fields_item = CustomField.from_dict(registrant_custom_fields_item_data)

            registrant_custom_fields.append(registrant_custom_fields_item)

        tickets = []
        _tickets = d.pop("tickets", UNSET)
        for tickets_item_data in _tickets or []:
            tickets_item = Ticket.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        _source = d.pop("source", UNSET)
        source: Union[Unset, IdNamePair]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = IdNamePair.from_dict(_source)

        event_registration_item = cls(
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
            id=id,
            event_id=event_id,
            registration_date_time=registration_date_time,
            coupon_code=coupon_code,
            send_system_email=send_system_email,
            registration_amount=registration_amount,
            ignore_capacity=ignore_capacity,
            registrant_account_id=registrant_account_id,
            fundraiser_account_id=fundraiser_account_id,
            registrant_custom_fields=registrant_custom_fields,
            tickets=tickets,
            source=source,
        )

        event_registration_item.additional_properties = d
        return event_registration_item

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
