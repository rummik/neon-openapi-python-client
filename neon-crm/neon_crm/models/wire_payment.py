from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirePayment")


@_attrs_define
class WirePayment:
    """
    Attributes:
        wire_number (Union[Unset, str]):
        institution (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        account_number (Union[Unset, str]):
        account_owner (Union[Unset, str]):
    """

    wire_number: Union[Unset, str] = UNSET
    institution: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    account_owner: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wire_number = self.wire_number

        institution = self.institution

        routing_number = self.routing_number

        account_number = self.account_number

        account_owner = self.account_owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wire_number is not UNSET:
            field_dict["wireNumber"] = wire_number
        if institution is not UNSET:
            field_dict["institution"] = institution
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if account_owner is not UNSET:
            field_dict["accountOwner"] = account_owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wire_number = d.pop("wireNumber", UNSET)

        institution = d.pop("institution", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        account_owner = d.pop("accountOwner", UNSET)

        wire_payment = cls(
            wire_number=wire_number,
            institution=institution,
            routing_number=routing_number,
            account_number=account_number,
            account_owner=account_owner,
        )

        wire_payment.additional_properties = d
        return wire_payment

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
