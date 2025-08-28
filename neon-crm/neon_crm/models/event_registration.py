from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.custom_field import CustomField
    from ..models.discount_item import DiscountItem
    from ..models.id_name_pair import IdNamePair
    from ..models.origin import Origin
    from ..models.payment import Payment
    from ..models.tax_deducible_info import TaxDeducibleInfo
    from ..models.ticket import Ticket


T = TypeVar("T", bound="EventRegistration")


@_attrs_define
class EventRegistration:
    """
    Attributes:
        event_id (str):
        registrant_account_id (str):
        id (Union[Unset, str]):
        registration_date_time (Union[Unset, str]):  Example: 2020-03-26T02:46:00Z.
        coupon_code (Union[Unset, str]):
        send_system_email (Union[Unset, bool]):
        registration_amount (Union[Unset, float]):
        ignore_capacity (Union[Unset, bool]):
        fundraiser_account_id (Union[Unset, str]):
        registrant_custom_fields (Union[Unset, list['CustomField']]):
        tickets (Union[Unset, list['Ticket']]):
        source (Union[Unset, IdNamePair]):
        origin (Union[Unset, Origin]):
        total_charge (Union[Unset, float]):
        total_discount (Union[Unset, float]):
        payments (Union[Unset, list['Payment']]):
        donor_covered_fee_flag (Union[Unset, bool]):
        donor_covered_fee (Union[Unset, float]):
        pay_later (Union[Unset, bool]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
        discounts (Union[Unset, list['DiscountItem']]):
    """

    event_id: str
    registrant_account_id: str
    id: Union[Unset, str] = UNSET
    registration_date_time: Union[Unset, str] = UNSET
    coupon_code: Union[Unset, str] = UNSET
    send_system_email: Union[Unset, bool] = UNSET
    registration_amount: Union[Unset, float] = UNSET
    ignore_capacity: Union[Unset, bool] = UNSET
    fundraiser_account_id: Union[Unset, str] = UNSET
    registrant_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    tickets: Union[Unset, list["Ticket"]] = UNSET
    source: Union[Unset, "IdNamePair"] = UNSET
    origin: Union[Unset, "Origin"] = UNSET
    total_charge: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    payments: Union[Unset, list["Payment"]] = UNSET
    donor_covered_fee_flag: Union[Unset, bool] = UNSET
    donor_covered_fee: Union[Unset, float] = UNSET
    pay_later: Union[Unset, bool] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    discounts: Union[Unset, list["DiscountItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        registrant_account_id = self.registrant_account_id

        id = self.id

        registration_date_time = self.registration_date_time

        coupon_code = self.coupon_code

        send_system_email = self.send_system_email

        registration_amount = self.registration_amount

        ignore_capacity = self.ignore_capacity

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

        origin: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        total_charge = self.total_charge

        total_discount = self.total_discount

        payments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)

        donor_covered_fee_flag = self.donor_covered_fee_flag

        donor_covered_fee = self.donor_covered_fee

        pay_later = self.pay_later

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        discounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventId": event_id,
                "registrantAccountId": registrant_account_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
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
        if fundraiser_account_id is not UNSET:
            field_dict["fundraiserAccountId"] = fundraiser_account_id
        if registrant_custom_fields is not UNSET:
            field_dict["registrantCustomFields"] = registrant_custom_fields
        if tickets is not UNSET:
            field_dict["tickets"] = tickets
        if source is not UNSET:
            field_dict["source"] = source
        if origin is not UNSET:
            field_dict["origin"] = origin
        if total_charge is not UNSET:
            field_dict["totalCharge"] = total_charge
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if payments is not UNSET:
            field_dict["payments"] = payments
        if donor_covered_fee_flag is not UNSET:
            field_dict["donorCoveredFeeFlag"] = donor_covered_fee_flag
        if donor_covered_fee is not UNSET:
            field_dict["donorCoveredFee"] = donor_covered_fee
        if pay_later is not UNSET:
            field_dict["payLater"] = pay_later
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info
        if discounts is not UNSET:
            field_dict["discounts"] = discounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.custom_field import CustomField
        from ..models.discount_item import DiscountItem
        from ..models.id_name_pair import IdNamePair
        from ..models.origin import Origin
        from ..models.payment import Payment
        from ..models.tax_deducible_info import TaxDeducibleInfo
        from ..models.ticket import Ticket

        d = dict(src_dict)
        event_id = d.pop("eventId")

        registrant_account_id = d.pop("registrantAccountId")

        id = d.pop("id", UNSET)

        registration_date_time = d.pop("registrationDateTime", UNSET)

        coupon_code = d.pop("couponCode", UNSET)

        send_system_email = d.pop("sendSystemEmail", UNSET)

        registration_amount = d.pop("registrationAmount", UNSET)

        ignore_capacity = d.pop("ignoreCapacity", UNSET)

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

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Origin]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Origin.from_dict(_origin)

        total_charge = d.pop("totalCharge", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        payments = []
        _payments = d.pop("payments", UNSET)
        for payments_item_data in _payments or []:
            payments_item = Payment.from_dict(payments_item_data)

            payments.append(payments_item)

        donor_covered_fee_flag = d.pop("donorCoveredFeeFlag", UNSET)

        donor_covered_fee = d.pop("donorCoveredFee", UNSET)

        pay_later = d.pop("payLater", UNSET)

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

        discounts = []
        _discounts = d.pop("discounts", UNSET)
        for discounts_item_data in _discounts or []:
            discounts_item = DiscountItem.from_dict(discounts_item_data)

            discounts.append(discounts_item)

        event_registration = cls(
            event_id=event_id,
            registrant_account_id=registrant_account_id,
            id=id,
            registration_date_time=registration_date_time,
            coupon_code=coupon_code,
            send_system_email=send_system_email,
            registration_amount=registration_amount,
            ignore_capacity=ignore_capacity,
            fundraiser_account_id=fundraiser_account_id,
            registrant_custom_fields=registrant_custom_fields,
            tickets=tickets,
            source=source,
            origin=origin,
            total_charge=total_charge,
            total_discount=total_discount,
            payments=payments,
            donor_covered_fee_flag=donor_covered_fee_flag,
            donor_covered_fee=donor_covered_fee,
            pay_later=pay_later,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
            discounts=discounts,
        )

        event_registration.additional_properties = d
        return event_registration

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
