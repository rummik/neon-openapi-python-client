from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InKindPayment")


@_attrs_define
class InKindPayment:
    """
    Attributes:
        fair_market_value (Union[Unset, float]):
        ncc_description (Union[Unset, str]):
    """

    fair_market_value: Union[Unset, float] = UNSET
    ncc_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fair_market_value = self.fair_market_value

        ncc_description = self.ncc_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fair_market_value is not UNSET:
            field_dict["fairMarketValue"] = fair_market_value
        if ncc_description is not UNSET:
            field_dict["nccDescription"] = ncc_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fair_market_value = d.pop("fairMarketValue", UNSET)

        ncc_description = d.pop("nccDescription", UNSET)

        in_kind_payment = cls(
            fair_market_value=fair_market_value,
            ncc_description=ncc_description,
        )

        in_kind_payment.additional_properties = d
        return in_kind_payment

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
