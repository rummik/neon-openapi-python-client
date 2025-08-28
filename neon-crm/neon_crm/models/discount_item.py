from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discount_item_order_item_type import DiscountItemOrderItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscountItem")


@_attrs_define
class DiscountItem:
    """
    Attributes:
        order_item_id (Union[Unset, str]):
        order_item_name (Union[Unset, str]):
        order_item_type (Union[Unset, DiscountItemOrderItemType]):
        discount_id (Union[Unset, str]):
        discount_name (Union[Unset, str]):
        discount (Union[Unset, float]):
    """

    order_item_id: Union[Unset, str] = UNSET
    order_item_name: Union[Unset, str] = UNSET
    order_item_type: Union[Unset, DiscountItemOrderItemType] = UNSET
    discount_id: Union[Unset, str] = UNSET
    discount_name: Union[Unset, str] = UNSET
    discount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_item_id = self.order_item_id

        order_item_name = self.order_item_name

        order_item_type: Union[Unset, str] = UNSET
        if not isinstance(self.order_item_type, Unset):
            order_item_type = self.order_item_type.value

        discount_id = self.discount_id

        discount_name = self.discount_name

        discount = self.discount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_item_id is not UNSET:
            field_dict["orderItemId"] = order_item_id
        if order_item_name is not UNSET:
            field_dict["orderItemName"] = order_item_name
        if order_item_type is not UNSET:
            field_dict["orderItemType"] = order_item_type
        if discount_id is not UNSET:
            field_dict["discountId"] = discount_id
        if discount_name is not UNSET:
            field_dict["discountName"] = discount_name
        if discount is not UNSET:
            field_dict["discount"] = discount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_item_id = d.pop("orderItemId", UNSET)

        order_item_name = d.pop("orderItemName", UNSET)

        _order_item_type = d.pop("orderItemType", UNSET)
        order_item_type: Union[Unset, DiscountItemOrderItemType]
        if isinstance(_order_item_type, Unset):
            order_item_type = UNSET
        else:
            order_item_type = DiscountItemOrderItemType(_order_item_type)

        discount_id = d.pop("discountId", UNSET)

        discount_name = d.pop("discountName", UNSET)

        discount = d.pop("discount", UNSET)

        discount_item = cls(
            order_item_id=order_item_id,
            order_item_name=order_item_name,
            order_item_type=order_item_type,
            discount_id=discount_id,
            discount_name=discount_name,
            discount=discount,
        )

        discount_item.additional_properties = d
        return discount_item

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
