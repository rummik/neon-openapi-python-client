from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_registration_response_status import EventRegistrationResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_response import PaymentResponse


T = TypeVar("T", bound="EventRegistrationResponse")


@_attrs_define
class EventRegistrationResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        account_id (Union[Unset, str]):
        status (Union[Unset, EventRegistrationResponseStatus]):
        payment_response (Union[Unset, PaymentResponse]):
    """

    id: Union[Unset, int] = UNSET
    account_id: Union[Unset, str] = UNSET
    status: Union[Unset, EventRegistrationResponseStatus] = UNSET
    payment_response: Union[Unset, "PaymentResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_response, Unset):
            payment_response = self.payment_response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if status is not UNSET:
            field_dict["status"] = status
        if payment_response is not UNSET:
            field_dict["paymentResponse"] = payment_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_response import PaymentResponse

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EventRegistrationResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EventRegistrationResponseStatus(_status)

        _payment_response = d.pop("paymentResponse", UNSET)
        payment_response: Union[Unset, PaymentResponse]
        if isinstance(_payment_response, Unset):
            payment_response = UNSET
        else:
            payment_response = PaymentResponse.from_dict(_payment_response)

        event_registration_response = cls(
            id=id,
            account_id=account_id,
            status=status,
            payment_response=payment_response,
        )

        event_registration_response.additional_properties = d
        return event_registration_response

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
