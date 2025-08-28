from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_order_item_type import AccountOrderItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountOrderItem")


@_attrs_define
class AccountOrderItem:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        type_ (Union[Unset, AccountOrderItemType]):
        unit_price (Union[Unset, float]):
        quantity (Union[Unset, int]):
        price (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, AccountOrderItemType] = UNSET
    unit_price: Union[Unset, float] = UNSET
    quantity: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        unit_price = self.unit_price

        quantity = self.quantity

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AccountOrderItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AccountOrderItemType(_type_)

        unit_price = d.pop("unitPrice", UNSET)

        quantity = d.pop("quantity", UNSET)

        price = d.pop("price", UNSET)

        account_order_item = cls(
            id=id,
            name=name,
            type_=type_,
            unit_price=unit_price,
            quantity=quantity,
            price=price,
        )

        account_order_item.additional_properties = d
        return account_order_item

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
