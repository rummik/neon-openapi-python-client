from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SoftCredit")


@_attrs_define
class SoftCredit:
    """
    Attributes:
        id (Union[Unset, str]):
        recipient_account_id (Union[Unset, str]):
        amount (Union[Unset, float]):
        donation_id (Union[Unset, str]):
        event_registration_id (Union[Unset, str]):
        membership_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    recipient_account_id: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    donation_id: Union[Unset, str] = UNSET
    event_registration_id: Union[Unset, str] = UNSET
    membership_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipient_account_id = self.recipient_account_id

        amount = self.amount

        donation_id = self.donation_id

        event_registration_id = self.event_registration_id

        membership_id = self.membership_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if recipient_account_id is not UNSET:
            field_dict["recipientAccountId"] = recipient_account_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if donation_id is not UNSET:
            field_dict["donationId"] = donation_id
        if event_registration_id is not UNSET:
            field_dict["eventRegistrationId"] = event_registration_id
        if membership_id is not UNSET:
            field_dict["membershipId"] = membership_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        recipient_account_id = d.pop("recipientAccountId", UNSET)

        amount = d.pop("amount", UNSET)

        donation_id = d.pop("donationId", UNSET)

        event_registration_id = d.pop("eventRegistrationId", UNSET)

        membership_id = d.pop("membershipId", UNSET)

        soft_credit = cls(
            id=id,
            recipient_account_id=recipient_account_id,
            amount=amount,
            donation_id=donation_id,
            event_registration_id=event_registration_id,
            membership_id=membership_id,
        )

        soft_credit.additional_properties = d
        return soft_credit

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
