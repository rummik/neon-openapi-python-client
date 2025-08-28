from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_registration import EventRegistration
    from ..models.pagination import Pagination


T = TypeVar("T", bound="PaginationEventRegistration")


@_attrs_define
class PaginationEventRegistration:
    """
    Attributes:
        account_id (Union[Unset, str]):
        event_registrations (Union[Unset, list['EventRegistration']]):
        pagination (Union[Unset, Pagination]):
    """

    account_id: Union[Unset, str] = UNSET
    event_registrations: Union[Unset, list["EventRegistration"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        event_registrations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_registrations, Unset):
            event_registrations = []
            for event_registrations_item_data in self.event_registrations:
                event_registrations_item = event_registrations_item_data.to_dict()
                event_registrations.append(event_registrations_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if event_registrations is not UNSET:
            field_dict["eventRegistrations"] = event_registrations
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_registration import EventRegistration
        from ..models.pagination import Pagination

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        event_registrations = []
        _event_registrations = d.pop("eventRegistrations", UNSET)
        for event_registrations_item_data in _event_registrations or []:
            event_registrations_item = EventRegistration.from_dict(event_registrations_item_data)

            event_registrations.append(event_registrations_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        pagination_event_registration = cls(
            account_id=account_id,
            event_registrations=event_registrations,
            pagination=pagination,
        )

        pagination_event_registration.additional_properties = d
        return pagination_event_registration

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
