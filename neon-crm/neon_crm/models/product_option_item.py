from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_option_item_status import ProductOptionItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductOptionItem")


@_attrs_define
class ProductOptionItem:
    """
    Attributes:
        id (Union[Unset, str]):
        price_adjustment (Union[Unset, float]):
        advantage_amount_adjustment (Union[Unset, float]):
        non_deductible_amount_adjustment (Union[Unset, float]):
        name (Union[Unset, str]):
        status (Union[Unset, ProductOptionItemStatus]):
    """

    id: Union[Unset, str] = UNSET
    price_adjustment: Union[Unset, float] = UNSET
    advantage_amount_adjustment: Union[Unset, float] = UNSET
    non_deductible_amount_adjustment: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ProductOptionItemStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        price_adjustment = self.price_adjustment

        advantage_amount_adjustment = self.advantage_amount_adjustment

        non_deductible_amount_adjustment = self.non_deductible_amount_adjustment

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if price_adjustment is not UNSET:
            field_dict["priceAdjustment"] = price_adjustment
        if advantage_amount_adjustment is not UNSET:
            field_dict["advantageAmountAdjustment"] = advantage_amount_adjustment
        if non_deductible_amount_adjustment is not UNSET:
            field_dict["nonDeductibleAmountAdjustment"] = non_deductible_amount_adjustment
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        price_adjustment = d.pop("priceAdjustment", UNSET)

        advantage_amount_adjustment = d.pop("advantageAmountAdjustment", UNSET)

        non_deductible_amount_adjustment = d.pop("nonDeductibleAmountAdjustment", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProductOptionItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProductOptionItemStatus(_status)

        product_option_item = cls(
            id=id,
            price_adjustment=price_adjustment,
            advantage_amount_adjustment=advantage_amount_adjustment,
            non_deductible_amount_adjustment=non_deductible_amount_adjustment,
            name=name,
            status=status,
        )

        product_option_item.additional_properties = d
        return product_option_item

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
