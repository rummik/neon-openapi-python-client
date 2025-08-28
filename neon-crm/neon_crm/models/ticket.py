from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_attendee import EventAttendee


T = TypeVar("T", bound="Ticket")


@_attrs_define
class Ticket:
    """
    Attributes:
        ticket_id (Union[Unset, int]):
        ticket_sequence (Union[Unset, int]):
        attendees (Union[Unset, list['EventAttendee']]):
    """

    ticket_id: Union[Unset, int] = UNSET
    ticket_sequence: Union[Unset, int] = UNSET
    attendees: Union[Unset, list["EventAttendee"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticket_id = self.ticket_id

        ticket_sequence = self.ticket_sequence

        attendees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ticket_id is not UNSET:
            field_dict["ticketId"] = ticket_id
        if ticket_sequence is not UNSET:
            field_dict["ticketSequence"] = ticket_sequence
        if attendees is not UNSET:
            field_dict["attendees"] = attendees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_attendee import EventAttendee

        d = dict(src_dict)
        ticket_id = d.pop("ticketId", UNSET)

        ticket_sequence = d.pop("ticketSequence", UNSET)

        attendees = []
        _attendees = d.pop("attendees", UNSET)
        for attendees_item_data in _attendees or []:
            attendees_item = EventAttendee.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        ticket = cls(
            ticket_id=ticket_id,
            ticket_sequence=ticket_sequence,
            attendees=attendees,
        )

        ticket.additional_properties = d
        return ticket

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
