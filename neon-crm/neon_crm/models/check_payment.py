from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_payment_account_type import CheckPaymentAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckPayment")


@_attrs_define
class CheckPayment:
    """
    Attributes:
        institution (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        account_number (Union[Unset, str]):
        account_owner (Union[Unset, str]):
        check_number (Union[Unset, str]):
        account_type (Union[Unset, CheckPaymentAccountType]):
    """

    institution: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    account_owner: Union[Unset, str] = UNSET
    check_number: Union[Unset, str] = UNSET
    account_type: Union[Unset, CheckPaymentAccountType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        institution = self.institution

        routing_number = self.routing_number

        account_number = self.account_number

        account_owner = self.account_owner

        check_number = self.check_number

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if institution is not UNSET:
            field_dict["institution"] = institution
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if account_owner is not UNSET:
            field_dict["accountOwner"] = account_owner
        if check_number is not UNSET:
            field_dict["checkNumber"] = check_number
        if account_type is not UNSET:
            field_dict["accountType"] = account_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        institution = d.pop("institution", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        account_owner = d.pop("accountOwner", UNSET)

        check_number = d.pop("checkNumber", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, CheckPaymentAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = CheckPaymentAccountType(_account_type)

        check_payment = cls(
            institution=institution,
            routing_number=routing_number,
            account_number=account_number,
            account_owner=account_owner,
            check_number=check_number,
            account_type=account_type,
        )

        check_payment.additional_properties = d
        return check_payment

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
