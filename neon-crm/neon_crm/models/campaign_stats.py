from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignStats")


@_attrs_define
class CampaignStats:
    """
    Attributes:
        donation_count (Union[Unset, int]):
        donation_amount (Union[Unset, float]):
        pledge_count (Union[Unset, int]):
        pledge_amount (Union[Unset, float]):
        event_registration_count (Union[Unset, int]):
        event_registration_amount (Union[Unset, float]):
        grand_total (Union[Unset, float]):
    """

    donation_count: Union[Unset, int] = UNSET
    donation_amount: Union[Unset, float] = UNSET
    pledge_count: Union[Unset, int] = UNSET
    pledge_amount: Union[Unset, float] = UNSET
    event_registration_count: Union[Unset, int] = UNSET
    event_registration_amount: Union[Unset, float] = UNSET
    grand_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        donation_count = self.donation_count

        donation_amount = self.donation_amount

        pledge_count = self.pledge_count

        pledge_amount = self.pledge_amount

        event_registration_count = self.event_registration_count

        event_registration_amount = self.event_registration_amount

        grand_total = self.grand_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if donation_count is not UNSET:
            field_dict["donationCount"] = donation_count
        if donation_amount is not UNSET:
            field_dict["donationAmount"] = donation_amount
        if pledge_count is not UNSET:
            field_dict["pledgeCount"] = pledge_count
        if pledge_amount is not UNSET:
            field_dict["pledgeAmount"] = pledge_amount
        if event_registration_count is not UNSET:
            field_dict["eventRegistrationCount"] = event_registration_count
        if event_registration_amount is not UNSET:
            field_dict["eventRegistrationAmount"] = event_registration_amount
        if grand_total is not UNSET:
            field_dict["grandTotal"] = grand_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        donation_count = d.pop("donationCount", UNSET)

        donation_amount = d.pop("donationAmount", UNSET)

        pledge_count = d.pop("pledgeCount", UNSET)

        pledge_amount = d.pop("pledgeAmount", UNSET)

        event_registration_count = d.pop("eventRegistrationCount", UNSET)

        event_registration_amount = d.pop("eventRegistrationAmount", UNSET)

        grand_total = d.pop("grandTotal", UNSET)

        campaign_stats = cls(
            donation_count=donation_count,
            donation_amount=donation_amount,
            pledge_count=pledge_count,
            pledge_amount=pledge_amount,
            event_registration_count=event_registration_count,
            event_registration_amount=event_registration_amount,
            grand_total=grand_total,
        )

        campaign_stats.additional_properties = d
        return campaign_stats

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
