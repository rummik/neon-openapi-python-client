from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_check_payment_account_type import ECheckPaymentAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ECheckPayment")


@_attrs_define
class ECheckPayment:
    """
    Attributes:
        token (Union[Unset, str]):
        plaid_account_id (Union[Unset, str]):
        institution (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        account_number (Union[Unset, str]):
        account_owner (Union[Unset, str]):
        check_number (Union[Unset, str]):
        account_type (Union[Unset, ECheckPaymentAccountType]):
        transaction_number (Union[Unset, str]):
        account_holder_email (Union[Unset, str]):
    """

    token: Union[Unset, str] = UNSET
    plaid_account_id: Union[Unset, str] = UNSET
    institution: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    account_owner: Union[Unset, str] = UNSET
    check_number: Union[Unset, str] = UNSET
    account_type: Union[Unset, ECheckPaymentAccountType] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    account_holder_email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        plaid_account_id = self.plaid_account_id

        institution = self.institution

        routing_number = self.routing_number

        account_number = self.account_number

        account_owner = self.account_owner

        check_number = self.check_number

        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        transaction_number = self.transaction_number

        account_holder_email = self.account_holder_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if plaid_account_id is not UNSET:
            field_dict["plaidAccountId"] = plaid_account_id
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
        if transaction_number is not UNSET:
            field_dict["transactionNumber"] = transaction_number
        if account_holder_email is not UNSET:
            field_dict["accountHolderEmail"] = account_holder_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        plaid_account_id = d.pop("plaidAccountId", UNSET)

        institution = d.pop("institution", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        account_owner = d.pop("accountOwner", UNSET)

        check_number = d.pop("checkNumber", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, ECheckPaymentAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = ECheckPaymentAccountType(_account_type)

        transaction_number = d.pop("transactionNumber", UNSET)

        account_holder_email = d.pop("accountHolderEmail", UNSET)

        e_check_payment = cls(
            token=token,
            plaid_account_id=plaid_account_id,
            institution=institution,
            routing_number=routing_number,
            account_number=account_number,
            account_owner=account_owner,
            check_number=check_number,
            account_type=account_type,
            transaction_number=transaction_number,
            account_holder_email=account_holder_email,
        )

        e_check_payment.additional_properties = d
        return e_check_payment

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
