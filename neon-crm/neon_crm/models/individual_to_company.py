from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualToCompany")


@_attrs_define
class IndividualToCompany:
    """
    Attributes:
        individual_contact_id (Union[Unset, str]):
        company_account_id (Union[Unset, str]):
    """

    individual_contact_id: Union[Unset, str] = UNSET
    company_account_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        individual_contact_id = self.individual_contact_id

        company_account_id = self.company_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual_contact_id is not UNSET:
            field_dict["individualContactId"] = individual_contact_id
        if company_account_id is not UNSET:
            field_dict["companyAccountId"] = company_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        individual_contact_id = d.pop("individualContactId", UNSET)

        company_account_id = d.pop("companyAccountId", UNSET)

        individual_to_company = cls(
            individual_contact_id=individual_contact_id,
            company_account_id=company_account_id,
        )

        individual_to_company.additional_properties = d
        return individual_to_company

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
