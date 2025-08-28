import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="OrderShipping")


@_attrs_define
class OrderShipping:
    """
    Attributes:
        shipping_method_name (str):
        shipping_deliver_to (str):
        zip_code (str):
        address_line_1 (str):
        shipping_date (Union[Unset, datetime.date]):
        shipping_company_name (Union[Unset, str]):
        city (Union[Unset, str]):
        state_province (Union[Unset, CodeNamePair]):
        country (Union[Unset, IdNamePair]):
        county (Union[Unset, str]):
        zip_code_suffix (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        phone (Union[Unset, str]):
    """

    shipping_method_name: str
    shipping_deliver_to: str
    zip_code: str
    address_line_1: str
    shipping_date: Union[Unset, datetime.date] = UNSET
    shipping_company_name: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_province: Union[Unset, "CodeNamePair"] = UNSET
    country: Union[Unset, "IdNamePair"] = UNSET
    county: Union[Unset, str] = UNSET
    zip_code_suffix: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipping_method_name = self.shipping_method_name

        shipping_deliver_to = self.shipping_deliver_to

        zip_code = self.zip_code

        address_line_1 = self.address_line_1

        shipping_date: Union[Unset, str] = UNSET
        if not isinstance(self.shipping_date, Unset):
            shipping_date = self.shipping_date.isoformat()

        shipping_company_name = self.shipping_company_name

        city = self.city

        state_province: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.state_province, Unset):
            state_province = self.state_province.to_dict()

        country: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        county = self.county

        zip_code_suffix = self.zip_code_suffix

        address_line_2 = self.address_line_2

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shippingMethodName": shipping_method_name,
                "shippingDeliverTo": shipping_deliver_to,
                "zipCode": zip_code,
                "addressLine1": address_line_1,
            }
        )
        if shipping_date is not UNSET:
            field_dict["shippingDate"] = shipping_date
        if shipping_company_name is not UNSET:
            field_dict["shippingCompanyName"] = shipping_company_name
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["stateProvince"] = state_province
        if country is not UNSET:
            field_dict["country"] = country
        if county is not UNSET:
            field_dict["county"] = county
        if zip_code_suffix is not UNSET:
            field_dict["zipCodeSuffix"] = zip_code_suffix
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        shipping_method_name = d.pop("shippingMethodName")

        shipping_deliver_to = d.pop("shippingDeliverTo")

        zip_code = d.pop("zipCode")

        address_line_1 = d.pop("addressLine1")

        _shipping_date = d.pop("shippingDate", UNSET)
        shipping_date: Union[Unset, datetime.date]
        if isinstance(_shipping_date, Unset):
            shipping_date = UNSET
        else:
            shipping_date = isoparse(_shipping_date).date()

        shipping_company_name = d.pop("shippingCompanyName", UNSET)

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

        county = d.pop("county", UNSET)

        zip_code_suffix = d.pop("zipCodeSuffix", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        phone = d.pop("phone", UNSET)

        order_shipping = cls(
            shipping_method_name=shipping_method_name,
            shipping_deliver_to=shipping_deliver_to,
            zip_code=zip_code,
            address_line_1=address_line_1,
            shipping_date=shipping_date,
            shipping_company_name=shipping_company_name,
            city=city,
            state_province=state_province,
            country=country,
            county=county,
            zip_code_suffix=zip_code_suffix,
            address_line_2=address_line_2,
            phone=phone,
        )

        order_shipping.additional_properties = d
        return order_shipping

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
