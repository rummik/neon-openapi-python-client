from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_response import PaymentResponse


T = TypeVar("T", bound="PledgePaymentResponse")


@_attrs_define
class PledgePaymentResponse:
    """
    Attributes:
        pledge_payment_id (Union[Unset, str]):
        balance (Union[Unset, float]):
        total (Union[Unset, float]):
        installment_id (Union[Unset, str]):
        payment_response (Union[Unset, PaymentResponse]):
    """

    pledge_payment_id: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    installment_id: Union[Unset, str] = UNSET
    payment_response: Union[Unset, "PaymentResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pledge_payment_id = self.pledge_payment_id

        balance = self.balance

        total = self.total

        installment_id = self.installment_id

        payment_response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_response, Unset):
            payment_response = self.payment_response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pledge_payment_id is not UNSET:
            field_dict["pledgePaymentId"] = pledge_payment_id
        if balance is not UNSET:
            field_dict["balance"] = balance
        if total is not UNSET:
            field_dict["total"] = total
        if installment_id is not UNSET:
            field_dict["installmentId"] = installment_id
        if payment_response is not UNSET:
            field_dict["paymentResponse"] = payment_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_response import PaymentResponse

        d = dict(src_dict)
        pledge_payment_id = d.pop("pledgePaymentId", UNSET)

        balance = d.pop("balance", UNSET)

        total = d.pop("total", UNSET)

        installment_id = d.pop("installmentId", UNSET)

        _payment_response = d.pop("paymentResponse", UNSET)
        payment_response: Union[Unset, PaymentResponse]
        if isinstance(_payment_response, Unset):
            payment_response = UNSET
        else:
            payment_response = PaymentResponse.from_dict(_payment_response)

        pledge_payment_response = cls(
            pledge_payment_id=pledge_payment_id,
            balance=balance,
            total=total,
            installment_id=installment_id,
            payment_response=payment_response,
        )

        pledge_payment_response.additional_properties = d
        return pledge_payment_response

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
