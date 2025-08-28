import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.account_order_status import AccountOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_order_item import AccountOrderItem
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="AccountOrder")


@_attrs_define
class AccountOrder:
    """
    Attributes:
        order_date (datetime.date):
        account_id (str):
        id (Union[Unset, str]):
        items (Union[Unset, list['AccountOrderItem']]):
        total_charge (Union[Unset, float]):
        sub_total (Union[Unset, float]):
        tax (Union[Unset, float]):
        total_discount (Union[Unset, float]):
        shipping_handling_fee (Union[Unset, float]):
        status (Union[Unset, AccountOrderStatus]):
        timestamps (Union[Unset, Timestamps]):
    """

    order_date: datetime.date
    account_id: str
    id: Union[Unset, str] = UNSET
    items: Union[Unset, list["AccountOrderItem"]] = UNSET
    total_charge: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    shipping_handling_fee: Union[Unset, float] = UNSET
    status: Union[Unset, AccountOrderStatus] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_date = self.order_date.isoformat()

        account_id = self.account_id

        id = self.id

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        total_charge = self.total_charge

        sub_total = self.sub_total

        tax = self.tax

        total_discount = self.total_discount

        shipping_handling_fee = self.shipping_handling_fee

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderDate": order_date,
                "accountId": account_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items
        if total_charge is not UNSET:
            field_dict["totalCharge"] = total_charge
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if tax is not UNSET:
            field_dict["tax"] = tax
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if shipping_handling_fee is not UNSET:
            field_dict["shippingHandlingFee"] = shipping_handling_fee
        if status is not UNSET:
            field_dict["status"] = status
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_order_item import AccountOrderItem
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        order_date = isoparse(d.pop("orderDate")).date()

        account_id = d.pop("accountId")

        id = d.pop("id", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = AccountOrderItem.from_dict(items_item_data)

            items.append(items_item)

        total_charge = d.pop("totalCharge", UNSET)

        sub_total = d.pop("subTotal", UNSET)

        tax = d.pop("tax", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        shipping_handling_fee = d.pop("shippingHandlingFee", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AccountOrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AccountOrderStatus(_status)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        account_order = cls(
            order_date=order_date,
            account_id=account_id,
            id=id,
            items=items,
            total_charge=total_charge,
            sub_total=sub_total,
            tax=tax,
            total_discount=total_discount,
            shipping_handling_fee=shipping_handling_fee,
            status=status,
            timestamps=timestamps,
        )

        account_order.additional_properties = d
        return account_order

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
