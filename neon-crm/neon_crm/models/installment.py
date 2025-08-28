from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Installment")


@_attrs_define
class Installment:
    """
    Attributes:
        expected_date (str): Example: 2021-01-20
        amount (float):
        id (Union[Unset, str]):
        pledge_id (Union[Unset, str]):
        pledge_payment_ids (Union[Unset, list[str]]):
    """

    expected_date: str
    amount: float
    id: Union[Unset, str] = UNSET
    pledge_id: Union[Unset, str] = UNSET
    pledge_payment_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_date = self.expected_date

        amount = self.amount

        id = self.id

        pledge_id = self.pledge_id

        pledge_payment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pledge_payment_ids, Unset):
            pledge_payment_ids = self.pledge_payment_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expectedDate": expected_date,
                "amount": amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if pledge_id is not UNSET:
            field_dict["pledgeId"] = pledge_id
        if pledge_payment_ids is not UNSET:
            field_dict["pledgePaymentIds"] = pledge_payment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_date = d.pop("expectedDate")

        amount = d.pop("amount")

        id = d.pop("id", UNSET)

        pledge_id = d.pop("pledgeId", UNSET)

        pledge_payment_ids = cast(list[str], d.pop("pledgePaymentIds", UNSET))

        installment = cls(
            expected_date=expected_date,
            amount=amount,
            id=id,
            pledge_id=pledge_id,
            pledge_payment_ids=pledge_payment_ids,
        )

        installment.additional_properties = d
        return installment

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
