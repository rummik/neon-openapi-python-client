from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_address import BillingAddress


T = TypeVar("T", bound="CreditCardOnlinePayment")


@_attrs_define
class CreditCardOnlinePayment:
    """
    Attributes:
        token (Union[Unset, str]):
        card_number_last_four (Union[Unset, str]):
        expiration_month (Union[Unset, int]):
        expiration_year (Union[Unset, int]):
        card_type_code (Union[Unset, str]):
        card_holder_name (Union[Unset, str]):
        card_holder_email (Union[Unset, str]):
        billing_address (Union[Unset, BillingAddress]):
        transaction_number (Union[Unset, str]):
    """

    token: Union[Unset, str] = UNSET
    card_number_last_four: Union[Unset, str] = UNSET
    expiration_month: Union[Unset, int] = UNSET
    expiration_year: Union[Unset, int] = UNSET
    card_type_code: Union[Unset, str] = UNSET
    card_holder_name: Union[Unset, str] = UNSET
    card_holder_email: Union[Unset, str] = UNSET
    billing_address: Union[Unset, "BillingAddress"] = UNSET
    transaction_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        card_number_last_four = self.card_number_last_four

        expiration_month = self.expiration_month

        expiration_year = self.expiration_year

        card_type_code = self.card_type_code

        card_holder_name = self.card_holder_name

        card_holder_email = self.card_holder_email

        billing_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        transaction_number = self.transaction_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if card_number_last_four is not UNSET:
            field_dict["cardNumberLastFour"] = card_number_last_four
        if expiration_month is not UNSET:
            field_dict["expirationMonth"] = expiration_month
        if expiration_year is not UNSET:
            field_dict["expirationYear"] = expiration_year
        if card_type_code is not UNSET:
            field_dict["cardTypeCode"] = card_type_code
        if card_holder_name is not UNSET:
            field_dict["cardHolderName"] = card_holder_name
        if card_holder_email is not UNSET:
            field_dict["cardHolderEmail"] = card_holder_email
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if transaction_number is not UNSET:
            field_dict["transactionNumber"] = transaction_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_address import BillingAddress

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        card_number_last_four = d.pop("cardNumberLastFour", UNSET)

        expiration_month = d.pop("expirationMonth", UNSET)

        expiration_year = d.pop("expirationYear", UNSET)

        card_type_code = d.pop("cardTypeCode", UNSET)

        card_holder_name = d.pop("cardHolderName", UNSET)

        card_holder_email = d.pop("cardHolderEmail", UNSET)

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: Union[Unset, BillingAddress]
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BillingAddress.from_dict(_billing_address)

        transaction_number = d.pop("transactionNumber", UNSET)

        credit_card_online_payment = cls(
            token=token,
            card_number_last_four=card_number_last_four,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            card_type_code=card_type_code,
            card_holder_name=card_holder_name,
            card_holder_email=card_holder_email,
            billing_address=billing_address,
            transaction_number=transaction_number,
        )

        credit_card_online_payment.additional_properties = d
        return credit_card_online_payment

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
