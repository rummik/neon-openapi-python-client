from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tickets_per_registration_operator import TicketsPerRegistrationOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="TicketsPerRegistration")


@_attrs_define
class TicketsPerRegistration:
    """
    Attributes:
        number (Union[Unset, int]):
        operator (Union[Unset, TicketsPerRegistrationOperator]):
    """

    number: Union[Unset, int] = UNSET
    operator: Union[Unset, TicketsPerRegistrationOperator] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, TicketsPerRegistrationOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = TicketsPerRegistrationOperator(_operator)

        tickets_per_registration = cls(
            number=number,
            operator=operator,
        )

        tickets_per_registration.additional_properties = d
        return tickets_per_registration

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
