from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discount_item import DiscountItem


T = TypeVar("T", bound="MembershipCalculateResult")


@_attrs_define
class MembershipCalculateResult:
    """
    Attributes:
        sub_total (Union[Unset, float]):
        total_discount (Union[Unset, float]):
        total_charge (Union[Unset, float]):
        discounts (Union[Unset, list['DiscountItem']]):
    """

    sub_total: Union[Unset, float] = UNSET
    total_discount: Union[Unset, float] = UNSET
    total_charge: Union[Unset, float] = UNSET
    discounts: Union[Unset, list["DiscountItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub_total = self.sub_total

        total_discount = self.total_discount

        total_charge = self.total_charge

        discounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_total is not UNSET:
            field_dict["subTotal"] = sub_total
        if total_discount is not UNSET:
            field_dict["totalDiscount"] = total_discount
        if total_charge is not UNSET:
            field_dict["totalCharge"] = total_charge
        if discounts is not UNSET:
            field_dict["discounts"] = discounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discount_item import DiscountItem

        d = dict(src_dict)
        sub_total = d.pop("subTotal", UNSET)

        total_discount = d.pop("totalDiscount", UNSET)

        total_charge = d.pop("totalCharge", UNSET)

        discounts = []
        _discounts = d.pop("discounts", UNSET)
        for discounts_item_data in _discounts or []:
            discounts_item = DiscountItem.from_dict(discounts_item_data)

            discounts.append(discounts_item)

        membership_calculate_result = cls(
            sub_total=sub_total,
            total_discount=total_discount,
            total_charge=total_charge,
            discounts=discounts,
        )

        membership_calculate_result.additional_properties = d
        return membership_calculate_result

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
