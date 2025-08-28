from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dyna_recurring_donation import DynaRecurringDonation
    from ..models.pagination import Pagination


T = TypeVar("T", bound="RecurringDonationsResponse")


@_attrs_define
class RecurringDonationsResponse:
    """
    Attributes:
        recurring_donations (Union[Unset, list['DynaRecurringDonation']]):
        pagination (Union[Unset, Pagination]):
    """

    recurring_donations: Union[Unset, list["DynaRecurringDonation"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recurring_donations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recurring_donations, Unset):
            recurring_donations = []
            for recurring_donations_item_data in self.recurring_donations:
                recurring_donations_item = recurring_donations_item_data.to_dict()
                recurring_donations.append(recurring_donations_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recurring_donations is not UNSET:
            field_dict["recurringDonations"] = recurring_donations
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dyna_recurring_donation import DynaRecurringDonation
        from ..models.pagination import Pagination

        d = dict(src_dict)
        recurring_donations = []
        _recurring_donations = d.pop("recurringDonations", UNSET)
        for recurring_donations_item_data in _recurring_donations or []:
            recurring_donations_item = DynaRecurringDonation.from_dict(recurring_donations_item_data)

            recurring_donations.append(recurring_donations_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        recurring_donations_response = cls(
            recurring_donations=recurring_donations,
            pagination=pagination,
        )

        recurring_donations_response.additional_properties = d
        return recurring_donations_response

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
