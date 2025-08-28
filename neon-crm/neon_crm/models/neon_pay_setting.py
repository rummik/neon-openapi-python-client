from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NeonPaySetting")


@_attrs_define
class NeonPaySetting:
    """
    Attributes:
        merchant_id (Union[Unset, str]):
        public_key (Union[Unset, str]):
    """

    merchant_id: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merchant_id = self.merchant_id

        public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merchant_id is not UNSET:
            field_dict["merchantId"] = merchant_id
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        merchant_id = d.pop("merchantId", UNSET)

        public_key = d.pop("publicKey", UNSET)

        neon_pay_setting = cls(
            merchant_id=merchant_id,
            public_key=public_key,
        )

        neon_pay_setting.additional_properties = d
        return neon_pay_setting

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
