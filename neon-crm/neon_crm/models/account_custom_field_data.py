from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_custom_field_data_account_type import AccountCustomFieldDataAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountCustomFieldData")


@_attrs_define
class AccountCustomFieldData:
    """
    Attributes:
        account_type (Union[Unset, AccountCustomFieldDataAccountType]):
    """

    account_type: Union[Unset, AccountCustomFieldDataAccountType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["accountType"] = account_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, AccountCustomFieldDataAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountCustomFieldDataAccountType(_account_type)

        account_custom_field_data = cls(
            account_type=account_type,
        )

        account_custom_field_data.additional_properties = d
        return account_custom_field_data

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
