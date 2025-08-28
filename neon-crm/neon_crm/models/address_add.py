from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_add_fax_type import AddressAddFaxType
from ..models.address_add_phone_1_type import AddressAddPhone1Type
from ..models.address_add_phone_2_type import AddressAddPhone2Type
from ..models.address_add_phone_3_type import AddressAddPhone3Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="AddressAdd")


@_attrs_define
class AddressAdd:
    """
    Attributes:
        account_id (Union[Unset, str]):
        address_id (Union[Unset, str]):
        is_primary_address (Union[Unset, bool]):
        contact_id (Union[Unset, str]):
        type_ (Union[Unset, IdNamePair]):
        valid_address (Union[Unset, bool]):
        address_line_1 (Union[Unset, str]):
        start_date (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        end_date (Union[Unset, str]):
        address_line_3 (Union[Unset, str]):
        address_line_4 (Union[Unset, str]):
        city (Union[Unset, str]):
        state_province (Union[Unset, CodeNamePair]):
        country (Union[Unset, IdNamePair]):
        territory (Union[Unset, str]):
        county (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        zip_code_suffix (Union[Unset, str]):
        phone1 (Union[Unset, str]):
        phone_1_type (Union[Unset, AddressAddPhone1Type]):
        phone2 (Union[Unset, str]):
        phone_2_type (Union[Unset, AddressAddPhone2Type]):
        phone3 (Union[Unset, str]):
        phone_3_type (Union[Unset, AddressAddPhone3Type]):
        fax (Union[Unset, str]):
        fax_type (Union[Unset, AddressAddFaxType]):
    """

    account_id: Union[Unset, str] = UNSET
    address_id: Union[Unset, str] = UNSET
    is_primary_address: Union[Unset, bool] = UNSET
    contact_id: Union[Unset, str] = UNSET
    type_: Union[Unset, "IdNamePair"] = UNSET
    valid_address: Union[Unset, bool] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    address_line_3: Union[Unset, str] = UNSET
    address_line_4: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_province: Union[Unset, "CodeNamePair"] = UNSET
    country: Union[Unset, "IdNamePair"] = UNSET
    territory: Union[Unset, str] = UNSET
    county: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    zip_code_suffix: Union[Unset, str] = UNSET
    phone1: Union[Unset, str] = UNSET
    phone_1_type: Union[Unset, AddressAddPhone1Type] = UNSET
    phone2: Union[Unset, str] = UNSET
    phone_2_type: Union[Unset, AddressAddPhone2Type] = UNSET
    phone3: Union[Unset, str] = UNSET
    phone_3_type: Union[Unset, AddressAddPhone3Type] = UNSET
    fax: Union[Unset, str] = UNSET
    fax_type: Union[Unset, AddressAddFaxType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        address_id = self.address_id

        is_primary_address = self.is_primary_address

        contact_id = self.contact_id

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        valid_address = self.valid_address

        address_line_1 = self.address_line_1

        start_date = self.start_date

        address_line_2 = self.address_line_2

        end_date = self.end_date

        address_line_3 = self.address_line_3

        address_line_4 = self.address_line_4

        city = self.city

        state_province: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.state_province, Unset):
            state_province = self.state_province.to_dict()

        country: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        territory = self.territory

        county = self.county

        zip_code = self.zip_code

        zip_code_suffix = self.zip_code_suffix

        phone1 = self.phone1

        phone_1_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_1_type, Unset):
            phone_1_type = self.phone_1_type.value

        phone2 = self.phone2

        phone_2_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_2_type, Unset):
            phone_2_type = self.phone_2_type.value

        phone3 = self.phone3

        phone_3_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_3_type, Unset):
            phone_3_type = self.phone_3_type.value

        fax = self.fax

        fax_type: Union[Unset, str] = UNSET
        if not isinstance(self.fax_type, Unset):
            fax_type = self.fax_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
        if is_primary_address is not UNSET:
            field_dict["isPrimaryAddress"] = is_primary_address
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if valid_address is not UNSET:
            field_dict["validAddress"] = valid_address
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if address_line_3 is not UNSET:
            field_dict["addressLine3"] = address_line_3
        if address_line_4 is not UNSET:
            field_dict["addressLine4"] = address_line_4
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["stateProvince"] = state_province
        if country is not UNSET:
            field_dict["country"] = country
        if territory is not UNSET:
            field_dict["territory"] = territory
        if county is not UNSET:
            field_dict["county"] = county
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if zip_code_suffix is not UNSET:
            field_dict["zipCodeSuffix"] = zip_code_suffix
        if phone1 is not UNSET:
            field_dict["phone1"] = phone1
        if phone_1_type is not UNSET:
            field_dict["phone1Type"] = phone_1_type
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if phone_2_type is not UNSET:
            field_dict["phone2Type"] = phone_2_type
        if phone3 is not UNSET:
            field_dict["phone3"] = phone3
        if phone_3_type is not UNSET:
            field_dict["phone3Type"] = phone_3_type
        if fax is not UNSET:
            field_dict["fax"] = fax
        if fax_type is not UNSET:
            field_dict["faxType"] = fax_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        address_id = d.pop("addressId", UNSET)

        is_primary_address = d.pop("isPrimaryAddress", UNSET)

        contact_id = d.pop("contactId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, IdNamePair]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = IdNamePair.from_dict(_type_)

        valid_address = d.pop("validAddress", UNSET)

        address_line_1 = d.pop("addressLine1", UNSET)

        start_date = d.pop("startDate", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        end_date = d.pop("endDate", UNSET)

        address_line_3 = d.pop("addressLine3", UNSET)

        address_line_4 = d.pop("addressLine4", UNSET)

        city = d.pop("city", UNSET)

        _state_province = d.pop("stateProvince", UNSET)
        state_province: Union[Unset, CodeNamePair]
        if isinstance(_state_province, Unset):
            state_province = UNSET
        else:
            state_province = CodeNamePair.from_dict(_state_province)

        _country = d.pop("country", UNSET)
        country: Union[Unset, IdNamePair]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = IdNamePair.from_dict(_country)

        territory = d.pop("territory", UNSET)

        county = d.pop("county", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        zip_code_suffix = d.pop("zipCodeSuffix", UNSET)

        phone1 = d.pop("phone1", UNSET)

        _phone_1_type = d.pop("phone1Type", UNSET)
        phone_1_type: Union[Unset, AddressAddPhone1Type]
        if isinstance(_phone_1_type, Unset):
            phone_1_type = UNSET
        else:
            phone_1_type = AddressAddPhone1Type(_phone_1_type)

        phone2 = d.pop("phone2", UNSET)

        _phone_2_type = d.pop("phone2Type", UNSET)
        phone_2_type: Union[Unset, AddressAddPhone2Type]
        if isinstance(_phone_2_type, Unset):
            phone_2_type = UNSET
        else:
            phone_2_type = AddressAddPhone2Type(_phone_2_type)

        phone3 = d.pop("phone3", UNSET)

        _phone_3_type = d.pop("phone3Type", UNSET)
        phone_3_type: Union[Unset, AddressAddPhone3Type]
        if isinstance(_phone_3_type, Unset):
            phone_3_type = UNSET
        else:
            phone_3_type = AddressAddPhone3Type(_phone_3_type)

        fax = d.pop("fax", UNSET)

        _fax_type = d.pop("faxType", UNSET)
        fax_type: Union[Unset, AddressAddFaxType]
        if isinstance(_fax_type, Unset):
            fax_type = UNSET
        else:
            fax_type = AddressAddFaxType(_fax_type)

        address_add = cls(
            account_id=account_id,
            address_id=address_id,
            is_primary_address=is_primary_address,
            contact_id=contact_id,
            type_=type_,
            valid_address=valid_address,
            address_line_1=address_line_1,
            start_date=start_date,
            address_line_2=address_line_2,
            end_date=end_date,
            address_line_3=address_line_3,
            address_line_4=address_line_4,
            city=city,
            state_province=state_province,
            country=country,
            territory=territory,
            county=county,
            zip_code=zip_code,
            zip_code_suffix=zip_code_suffix,
            phone1=phone1,
            phone_1_type=phone_1_type,
            phone2=phone2,
            phone_2_type=phone_2_type,
            phone3=phone3,
            phone_3_type=phone_3_type,
            fax=fax,
            fax_type=fax_type,
        )

        address_add.additional_properties = d
        return address_add

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
