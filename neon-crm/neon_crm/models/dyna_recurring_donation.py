from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynaRecurringDonation")


@_attrs_define
class DynaRecurringDonation:
    """
    Attributes:
        id (Union[Unset, int]):
        account_id (Union[Unset, str]):
        donor_name (Union[Unset, str]):
        amount (Union[Unset, float]):
        frequency (Union[Unset, str]):
        next_date (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    account_id: Union[Unset, str] = UNSET
    donor_name: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    frequency: Union[Unset, str] = UNSET
    next_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        donor_name = self.donor_name

        amount = self.amount

        frequency = self.frequency

        next_date = self.next_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if donor_name is not UNSET:
            field_dict["donorName"] = donor_name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if next_date is not UNSET:
            field_dict["nextDate"] = next_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        donor_name = d.pop("donorName", UNSET)

        amount = d.pop("amount", UNSET)

        frequency = d.pop("frequency", UNSET)

        next_date = d.pop("nextDate", UNSET)

        dyna_recurring_donation = cls(
            id=id,
            account_id=account_id,
            donor_name=donor_name,
            amount=amount,
            frequency=frequency,
            next_date=next_date,
        )

        dyna_recurring_donation.additional_properties = d
        return dyna_recurring_donation

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
