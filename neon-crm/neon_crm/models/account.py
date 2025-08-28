from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_account import CompanyAccount
    from ..models.individual_account import IndividualAccount


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        individual_account (Union[Unset, IndividualAccount]):
        company_account (Union[Unset, CompanyAccount]):
    """

    individual_account: Union[Unset, "IndividualAccount"] = UNSET
    company_account: Union[Unset, "CompanyAccount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        individual_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.individual_account, Unset):
            individual_account = self.individual_account.to_dict()

        company_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company_account, Unset):
            company_account = self.company_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual_account is not UNSET:
            field_dict["individualAccount"] = individual_account
        if company_account is not UNSET:
            field_dict["companyAccount"] = company_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_account import CompanyAccount
        from ..models.individual_account import IndividualAccount

        d = dict(src_dict)
        _individual_account = d.pop("individualAccount", UNSET)
        individual_account: Union[Unset, IndividualAccount]
        if isinstance(_individual_account, Unset):
            individual_account = UNSET
        else:
            individual_account = IndividualAccount.from_dict(_individual_account)

        _company_account = d.pop("companyAccount", UNSET)
        company_account: Union[Unset, CompanyAccount]
        if isinstance(_company_account, Unset):
            company_account = UNSET
        else:
            company_account = CompanyAccount.from_dict(_company_account)

        account = cls(
            individual_account=individual_account,
            company_account=company_account,
        )

        account.additional_properties = d
        return account

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
