import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.code_name_pair import CodeNamePair
    from ..models.dob import Dob


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        account_id (Union[Unset, str]):
        contact_id (Union[Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        prefix (Union[Unset, str]):
        suffix (Union[Unset, str]):
        salutation (Union[Unset, str]):
        preferred_name (Union[Unset, str]):
        dob (Union[Unset, Dob]):
        gender (Union[Unset, CodeNamePair]):
        email1 (Union[Unset, str]):
        email2 (Union[Unset, str]):
        email3 (Union[Unset, str]):
        deceased (Union[Unset, bool]):
        department (Union[Unset, str]):
        title (Union[Unset, str]):
        primary_contact (Union[Unset, bool]):
        current_employer (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        addresses (Union[Unset, list['Address']]):
    """

    account_id: Union[Unset, str] = UNSET
    contact_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    salutation: Union[Unset, str] = UNSET
    preferred_name: Union[Unset, str] = UNSET
    dob: Union[Unset, "Dob"] = UNSET
    gender: Union[Unset, "CodeNamePair"] = UNSET
    email1: Union[Unset, str] = UNSET
    email2: Union[Unset, str] = UNSET
    email3: Union[Unset, str] = UNSET
    deceased: Union[Unset, bool] = UNSET
    department: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    primary_contact: Union[Unset, bool] = UNSET
    current_employer: Union[Unset, bool] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    addresses: Union[Unset, list["Address"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        contact_id = self.contact_id

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        prefix = self.prefix

        suffix = self.suffix

        salutation = self.salutation

        preferred_name = self.preferred_name

        dob: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dob, Unset):
            dob = self.dob.to_dict()

        gender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        email1 = self.email1

        email2 = self.email2

        email3 = self.email3

        deceased = self.deceased

        department = self.department

        title = self.title

        primary_contact = self.primary_contact

        current_employer = self.current_employer

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if preferred_name is not UNSET:
            field_dict["preferredName"] = preferred_name
        if dob is not UNSET:
            field_dict["dob"] = dob
        if gender is not UNSET:
            field_dict["gender"] = gender
        if email1 is not UNSET:
            field_dict["email1"] = email1
        if email2 is not UNSET:
            field_dict["email2"] = email2
        if email3 is not UNSET:
            field_dict["email3"] = email3
        if deceased is not UNSET:
            field_dict["deceased"] = deceased
        if department is not UNSET:
            field_dict["department"] = department
        if title is not UNSET:
            field_dict["title"] = title
        if primary_contact is not UNSET:
            field_dict["primaryContact"] = primary_contact
        if current_employer is not UNSET:
            field_dict["currentEmployer"] = current_employer
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.code_name_pair import CodeNamePair
        from ..models.dob import Dob

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        contact_id = d.pop("contactId", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        last_name = d.pop("lastName", UNSET)

        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        salutation = d.pop("salutation", UNSET)

        preferred_name = d.pop("preferredName", UNSET)

        _dob = d.pop("dob", UNSET)
        dob: Union[Unset, Dob]
        if isinstance(_dob, Unset):
            dob = UNSET
        else:
            dob = Dob.from_dict(_dob)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, CodeNamePair]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = CodeNamePair.from_dict(_gender)

        email1 = d.pop("email1", UNSET)

        email2 = d.pop("email2", UNSET)

        email3 = d.pop("email3", UNSET)

        deceased = d.pop("deceased", UNSET)

        department = d.pop("department", UNSET)

        title = d.pop("title", UNSET)

        primary_contact = d.pop("primaryContact", UNSET)

        current_employer = d.pop("currentEmployer", UNSET)

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

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = Address.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        contact = cls(
            account_id=account_id,
            contact_id=contact_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            prefix=prefix,
            suffix=suffix,
            salutation=salutation,
            preferred_name=preferred_name,
            dob=dob,
            gender=gender,
            email1=email1,
            email2=email2,
            email3=email3,
            deceased=deceased,
            department=department,
            title=title,
            primary_contact=primary_contact,
            current_employer=current_employer,
            start_date=start_date,
            end_date=end_date,
            addresses=addresses,
        )

        contact.additional_properties = d
        return contact

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
