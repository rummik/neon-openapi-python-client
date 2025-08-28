import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.order_status import OrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discount_item import DiscountItem
    from ..models.donation_item import DonationItem
    from ..models.event_registration_item import EventRegistrationItem
    from ..models.membership_item import MembershipItem
    from ..models.order_shipping import OrderShipping
    from ..models.payment import Payment
    from ..models.product_item import ProductItem
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """
    Attributes:
        order_date (datetime.date):
        account_id (str):
        donations (Union[Unset, list['DonationItem']]):
        id (Union[Unset, str]):
        event_registrations (Union[Unset, list['EventRegistrationItem']]):
        products (Union[Unset, list['ProductItem']]):
        memberships (Union[Unset, list['MembershipItem']]):
        total_charge (Union[Unset, float]):
        need_shipping (Union[Unset, bool]):
        sub_total (Union[Unset, float]):
        shipping (Union[Unset, OrderShipping]):
        tax (Union[Unset, float]):
        discounts (Union[Unset, list['DiscountItem']]):
        total_discount (Union[Unset, float]):
        donor_covered_fee_flag (Union[Unset, bool]):
        shipping_handling_fee (Union[Unset, float]):
        donor_covered_fee (Union[Unset, float]):
        status (Union[Unset, OrderStatus]):
        pay_later (Union[Unset, bool]): Write only
        timestamps (Union[Unset, Timestamps]):
        payments (Union[Unset, list['Payment']]):
    """

    order_date: datetime.date
    account_id: str
    donations: Union[Unset, list["DonationItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    event_registrations: Union[Unset, list["EventRegistrationItem"]] = UNSET
    products: Union[Unset, list["ProductItem"]] = UNSET
    memberships: Union[Unset, list["MembershipItem"]] = UNSET
    total_charge: Union[Unset, float] = UNSET
    need_shipping: Union[Unset, bool] = UNSET
    sub_total: Union[Unset, float] = UNSET
    shipping: Union[Unset, "OrderShipping"] = UNSET
    tax: Union[Unset, float] = UNSET
    discounts: Union[Unset, list["DiscountItem"]] = UNSET
    total_discount: Union[Unset, float] = UNSET
    donor_covered_fee_flag: Union[Unset, bool] = UNSET
    shipping_handling_fee: Union[Unset, float] = UNSET
    donor_covered_fee: Union[Unset, float] = UNSET
    status: Union[Unset, OrderStatus] = UNSET
    pay_later: Union[Unset, bool] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    payments: Union[Unset, list["Payment"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_date = self.order_date.isoformat()

        account_id = self.account_id

        donations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.donations, Unset):
            donations = []
            for donations_item_data in self.donations:
                donations_item = donations_item_data.to_dict()
                donations.append(donations_item)

        id = self.id

        event_registrations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_registrations, Unset):
            event_registrations = []
            for event_registrations_item_data in self.event_registrations:
                event_registrations_item = event_registrations_item_data.to_dict()
                event_registrations.append(event_registrations_item)

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        memberships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()
                memberships.append(memberships_item)

        total_charge = self.total_charge

        need_shipping = self.need_shipping

        sub_total = self.sub_total

        shipping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        tax = self.tax

        discounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        total_discount = self.total_discount

        donor_covered_fee_flag = self.donor_covered_fee_flag

        shipping_handling_fee = self.shipping_handling_fee

        donor_covered_fee = self.donor_covered_fee

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        pay_later = self.pay_later

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        payments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderDate": order_date,
                "accountId": account_id,
            }
        )
        if donations is not UNSET:
            field_dict["donations"] = donations
        if id is not UNSET:
            field_dict["id"] = id
        if event_registrations is not UNSET:
            field_dict["eventRegistrations"] = event_registrations
        if products is not UNSET:
            field_dict["products"] = products
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if total_charge is not UNSET:
            field_dict["totalCharge"] = total_charge
        if need_shipping is not UNSET:
            field_dict["needShipping"] = need_shipping
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if tax is not UNSET:
            field_dict["tax"] = tax
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if donor_covered_fee_flag is not UNSET:
            field_dict["donorCoveredFeeFlag"] = donor_covered_fee_flag
        if shipping_handling_fee is not UNSET:
            field_dict["shippingHandlingFee"] = shipping_handling_fee
        if donor_covered_fee is not UNSET:
            field_dict["donorCoveredFee"] = donor_covered_fee
        if status is not UNSET:
            field_dict["status"] = status
        if pay_later is not UNSET:
            field_dict["payLater"] = pay_later
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discount_item import DiscountItem
        from ..models.donation_item import DonationItem
        from ..models.event_registration_item import EventRegistrationItem
        from ..models.membership_item import MembershipItem
        from ..models.order_shipping import OrderShipping
        from ..models.payment import Payment
        from ..models.product_item import ProductItem
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        order_date = isoparse(d.pop("orderDate")).date()

        account_id = d.pop("accountId")

        donations = []
        _donations = d.pop("donations", UNSET)
        for donations_item_data in _donations or []:
            donations_item = DonationItem.from_dict(donations_item_data)

            donations.append(donations_item)

        id = d.pop("id", UNSET)

        event_registrations = []
        _event_registrations = d.pop("eventRegistrations", UNSET)
        for event_registrations_item_data in _event_registrations or []:
            event_registrations_item = EventRegistrationItem.from_dict(event_registrations_item_data)

            event_registrations.append(event_registrations_item)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = ProductItem.from_dict(products_item_data)

            products.append(products_item)

        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in _memberships or []:
            memberships_item = MembershipItem.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        total_charge = d.pop("totalCharge", UNSET)

        need_shipping = d.pop("needShipping", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, OrderShipping]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = OrderShipping.from_dict(_shipping)

        tax = d.pop("tax", UNSET)

        discounts = []
        _discounts = d.pop("discounts", UNSET)
        for discounts_item_data in _discounts or []:
            discounts_item = DiscountItem.from_dict(discounts_item_data)

            discounts.append(discounts_item)

        total_discount = d.pop("totalDiscount", UNSET)

        donor_covered_fee_flag = d.pop("donorCoveredFeeFlag", UNSET)

        shipping_handling_fee = d.pop("shippingHandlingFee", UNSET)

        donor_covered_fee = d.pop("donorCoveredFee", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderStatus(_status)

        pay_later = d.pop("payLater", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        payments = []
        _payments = d.pop("payments", UNSET)
        for payments_item_data in _payments or []:
            payments_item = Payment.from_dict(payments_item_data)

            payments.append(payments_item)

        order = cls(
            order_date=order_date,
            account_id=account_id,
            donations=donations,
            id=id,
            event_registrations=event_registrations,
            products=products,
            memberships=memberships,
            total_charge=total_charge,
            need_shipping=need_shipping,
            sub_total=sub_total,
            shipping=shipping,
            tax=tax,
            discounts=discounts,
            total_discount=total_discount,
            donor_covered_fee_flag=donor_covered_fee_flag,
            shipping_handling_fee=shipping_handling_fee,
            donor_covered_fee=donor_covered_fee,
            status=status,
            pay_later=pay_later,
            timestamps=timestamps,
            payments=payments,
        )

        order.additional_properties = d
        return order

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
