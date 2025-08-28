from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_response_status import PaymentResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentResponse")


@_attrs_define
class PaymentResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        status (Union[Unset, PaymentResponseStatus]):
        status_message (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, PaymentResponseStatus] = UNSET
    status_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message = self.status_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PaymentResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentResponseStatus(_status)

        status_message = d.pop("statusMessage", UNSET)

        payment_response = cls(
            id=id,
            status=status,
            status_message=status_message,
        )

        payment_response.additional_properties = d
        return payment_response

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
