from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_ticket_attendees_per_ticket_type import EventTicketAttendeesPerTicketType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.tax_deducible_info import TaxDeducibleInfo


T = TypeVar("T", bound="EventTicket")


@_attrs_define
class EventTicket:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        fee (Union[Unset, float]):
        max_number_available (Union[Unset, int]):
        number_remaining (Union[Unset, int]):
        attendees_per_ticket_type (Union[Unset, EventTicketAttendeesPerTicketType]):
        attendees_per_ticket_number (Union[Unset, int]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fee: Union[Unset, float] = UNSET
    max_number_available: Union[Unset, int] = UNSET
    number_remaining: Union[Unset, int] = UNSET
    attendees_per_ticket_type: Union[Unset, EventTicketAttendeesPerTicketType] = UNSET
    attendees_per_ticket_number: Union[Unset, int] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        fee = self.fee

        max_number_available = self.max_number_available

        number_remaining = self.number_remaining

        attendees_per_ticket_type: Union[Unset, str] = UNSET
        if not isinstance(self.attendees_per_ticket_type, Unset):
            attendees_per_ticket_type = self.attendees_per_ticket_type.value

        attendees_per_ticket_number = self.attendees_per_ticket_number

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if fee is not UNSET:
            field_dict["fee"] = fee
        if max_number_available is not UNSET:
            field_dict["maxNumberAvailable"] = max_number_available
        if number_remaining is not UNSET:
            field_dict["numberRemaining"] = number_remaining
        if attendees_per_ticket_type is not UNSET:
            field_dict["attendeesPerTicketType"] = attendees_per_ticket_type
        if attendees_per_ticket_number is not UNSET:
            field_dict["attendeesPerTicketNumber"] = attendees_per_ticket_number
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.tax_deducible_info import TaxDeducibleInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        fee = d.pop("fee", UNSET)

        max_number_available = d.pop("maxNumberAvailable", UNSET)

        number_remaining = d.pop("numberRemaining", UNSET)

        _attendees_per_ticket_type = d.pop("attendeesPerTicketType", UNSET)
        attendees_per_ticket_type: Union[Unset, EventTicketAttendeesPerTicketType]
        if isinstance(_attendees_per_ticket_type, Unset):
            attendees_per_ticket_type = UNSET
        else:
            attendees_per_ticket_type = EventTicketAttendeesPerTicketType(_attendees_per_ticket_type)

        attendees_per_ticket_number = d.pop("attendeesPerTicketNumber", UNSET)

        _cra_info = d.pop("craInfo", UNSET)
        cra_info: Union[Unset, CraInfo]
        if isinstance(_cra_info, Unset):
            cra_info = UNSET
        else:
            cra_info = CraInfo.from_dict(_cra_info)

        _tax_deductible_info = d.pop("taxDeductibleInfo", UNSET)
        tax_deductible_info: Union[Unset, TaxDeducibleInfo]
        if isinstance(_tax_deductible_info, Unset):
            tax_deductible_info = UNSET
        else:
            tax_deductible_info = TaxDeducibleInfo.from_dict(_tax_deductible_info)

        event_ticket = cls(
            id=id,
            name=name,
            description=description,
            fee=fee,
            max_number_available=max_number_available,
            number_remaining=number_remaining,
            attendees_per_ticket_type=attendees_per_ticket_type,
            attendees_per_ticket_number=attendees_per_ticket_number,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
        )

        event_ticket.additional_properties = d
        return event_ticket

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
