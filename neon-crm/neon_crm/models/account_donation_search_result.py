from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.donation import Donation
    from ..models.pagination import Pagination


T = TypeVar("T", bound="AccountDonationSearchResult")


@_attrs_define
class AccountDonationSearchResult:
    """
    Attributes:
        donations (Union[Unset, list['Donation']]):
        pagination (Union[Unset, Pagination]):
    """

    donations: Union[Unset, list["Donation"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        donations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.donations, Unset):
            donations = []
            for donations_item_data in self.donations:
                donations_item = donations_item_data.to_dict()
                donations.append(donations_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if donations is not UNSET:
            field_dict["donations"] = donations
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.donation import Donation
        from ..models.pagination import Pagination

        d = dict(src_dict)
        donations = []
        _donations = d.pop("donations", UNSET)
        for donations_item_data in _donations or []:
            donations_item = Donation.from_dict(donations_item_data)

            donations.append(donations_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        account_donation_search_result = cls(
            donations=donations,
            pagination=pagination,
        )

        account_donation_search_result.additional_properties = d
        return account_donation_search_result

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
