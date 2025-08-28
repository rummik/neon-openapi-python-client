from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_payment_request_transaction_type import AddPaymentRequestTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment import Payment


T = TypeVar("T", bound="AddPaymentRequest")


@_attrs_define
class AddPaymentRequest:
    """
    Attributes:
        transaction_id (str):
        transaction_type (AddPaymentRequestTransactionType):
        payment (Union[Unset, Payment]):
    """

    transaction_id: str
    transaction_type: AddPaymentRequestTransactionType
    payment: Union[Unset, "Payment"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id = self.transaction_id

        transaction_type = self.transaction_type.value

        payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactionId": transaction_id,
                "transactionType": transaction_type,
            }
        )
        if payment is not UNSET:
            field_dict["payment"] = payment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment import Payment

        d = dict(src_dict)
        transaction_id = d.pop("transactionId")

        transaction_type = AddPaymentRequestTransactionType(d.pop("transactionType"))

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, Payment]
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = Payment.from_dict(_payment)

        add_payment_request = cls(
            transaction_id=transaction_id,
            transaction_type=transaction_type,
            payment=payment,
        )

        add_payment_request.additional_properties = d
        return add_payment_request

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
