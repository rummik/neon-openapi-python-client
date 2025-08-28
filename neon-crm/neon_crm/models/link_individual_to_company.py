import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="LinkIndividualToCompany")


@_attrs_define
class LinkIndividualToCompany:
    """
    Attributes:
        individual_contact_id (Union[Unset, str]):
        is_primary_contact (Union[Unset, bool]):
        company_account_id (Union[Unset, str]):
        is_current_employee (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        address (Union[Unset, Address]):
        department (Union[Unset, str]):
        title (Union[Unset, str]):
        company_email (Union[Unset, str]):
    """

    individual_contact_id: Union[Unset, str] = UNSET
    is_primary_contact: Union[Unset, bool] = UNSET
    company_account_id: Union[Unset, str] = UNSET
    is_current_employee: Union[Unset, bool] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    address: Union[Unset, "Address"] = UNSET
    department: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    company_email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        individual_contact_id = self.individual_contact_id

        is_primary_contact = self.is_primary_contact

        company_account_id = self.company_account_id

        is_current_employee = self.is_current_employee

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        department = self.department

        title = self.title

        company_email = self.company_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual_contact_id is not UNSET:
            field_dict["individualContactId"] = individual_contact_id
        if is_primary_contact is not UNSET:
            field_dict["isPrimaryContact"] = is_primary_contact
        if company_account_id is not UNSET:
            field_dict["companyAccountId"] = company_account_id
        if is_current_employee is not UNSET:
            field_dict["isCurrentEmployee"] = is_current_employee
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if address is not UNSET:
            field_dict["address"] = address
        if department is not UNSET:
            field_dict["department"] = department
        if title is not UNSET:
            field_dict["title"] = title
        if company_email is not UNSET:
            field_dict["companyEmail"] = company_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address

        d = dict(src_dict)
        individual_contact_id = d.pop("individualContactId", UNSET)

        is_primary_contact = d.pop("isPrimaryContact", UNSET)

        company_account_id = d.pop("companyAccountId", UNSET)

        is_current_employee = d.pop("isCurrentEmployee", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        department = d.pop("department", UNSET)

        title = d.pop("title", UNSET)

        company_email = d.pop("companyEmail", UNSET)

        link_individual_to_company = cls(
            individual_contact_id=individual_contact_id,
            is_primary_contact=is_primary_contact,
            company_account_id=company_account_id,
            is_current_employee=is_current_employee,
            start_date=start_date,
            end_date=end_date,
            address=address,
            department=department,
            title=title,
            company_email=company_email,
        )

        link_individual_to_company.additional_properties = d
        return link_individual_to_company

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
