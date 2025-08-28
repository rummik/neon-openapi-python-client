from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_search_result_item_user_type import AccountSearchResultItemUserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountSearchResultItem")


@_attrs_define
class AccountSearchResultItem:
    """
    Attributes:
        account_id (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        email (Union[Unset, str]):
        user_type (Union[Unset, AccountSearchResultItemUserType]):
    """

    account_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    user_type: Union[Unset, AccountSearchResultItemUserType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        first_name = self.first_name

        last_name = self.last_name

        company_name = self.company_name

        email = self.email

        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if email is not UNSET:
            field_dict["email"] = email
        if user_type is not UNSET:
            field_dict["userType"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        company_name = d.pop("companyName", UNSET)

        email = d.pop("email", UNSET)

        _user_type = d.pop("userType", UNSET)
        user_type: Union[Unset, AccountSearchResultItemUserType]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = AccountSearchResultItemUserType(_user_type)

        account_search_result_item = cls(
            account_id=account_id,
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            email=email,
            user_type=user_type,
        )

        account_search_result_item.additional_properties = d
        return account_search_result_item

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
