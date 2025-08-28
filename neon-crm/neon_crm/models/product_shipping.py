from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductShipping")


@_attrs_define
class ProductShipping:
    """
    Attributes:
        shipping_required (Union[Unset, bool]):
        default_shipping_cost (Union[Unset, float]):
        pounds (Union[Unset, int]):
        ounces (Union[Unset, float]):
        days_to_ship (Union[Unset, int]):
    """

    shipping_required: Union[Unset, bool] = UNSET
    default_shipping_cost: Union[Unset, float] = UNSET
    pounds: Union[Unset, int] = UNSET
    ounces: Union[Unset, float] = UNSET
    days_to_ship: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping_required = self.shipping_required

        default_shipping_cost = self.default_shipping_cost

        pounds = self.pounds

        ounces = self.ounces

        days_to_ship = self.days_to_ship

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipping_required is not UNSET:
            field_dict["shippingRequired"] = shipping_required
        if default_shipping_cost is not UNSET:
            field_dict["defaultShippingCost"] = default_shipping_cost
        if pounds is not UNSET:
            field_dict["pounds"] = pounds
        if ounces is not UNSET:
            field_dict["ounces"] = ounces
        if days_to_ship is not UNSET:
            field_dict["daysToShip"] = days_to_ship

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shipping_required = d.pop("shippingRequired", UNSET)

        default_shipping_cost = d.pop("defaultShippingCost", UNSET)

        pounds = d.pop("pounds", UNSET)

        ounces = d.pop("ounces", UNSET)

        days_to_ship = d.pop("daysToShip", UNSET)

        product_shipping = cls(
            shipping_required=shipping_required,
            default_shipping_cost=default_shipping_cost,
            pounds=pounds,
            ounces=ounces,
            days_to_ship=days_to_ship,
        )

        product_shipping.additional_properties = d
        return product_shipping

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
