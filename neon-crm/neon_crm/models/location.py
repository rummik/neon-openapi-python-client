from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_name_pair import CodeNamePair
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """
    Attributes:
        name (Union[Unset, str]):
        room_number (Union[Unset, str]):
        building_number (Union[Unset, str]):
        address (Union[Unset, str]):
        city (Union[Unset, str]):
        state_province (Union[Unset, CodeNamePair]):
        country (Union[Unset, IdNamePair]):
        zip_code (Union[Unset, str]):
        zip_code_suffix (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    room_number: Union[Unset, str] = UNSET
    building_number: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_province: Union[Unset, "CodeNamePair"] = UNSET
    country: Union[Unset, "IdNamePair"] = UNSET
    zip_code: Union[Unset, str] = UNSET
    zip_code_suffix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        room_number = self.room_number

        building_number = self.building_number

        address = self.address

        city = self.city

        state_province: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.state_province, Unset):
            state_province = self.state_province.to_dict()

        country: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        zip_code = self.zip_code

        zip_code_suffix = self.zip_code_suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if room_number is not UNSET:
            field_dict["roomNumber"] = room_number
        if building_number is not UNSET:
            field_dict["buildingNumber"] = building_number
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if state_province is not UNSET:
            field_dict["stateProvince"] = state_province
        if country is not UNSET:
            field_dict["country"] = country
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if zip_code_suffix is not UNSET:
            field_dict["zipCodeSuffix"] = zip_code_suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_name_pair import CodeNamePair
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        room_number = d.pop("roomNumber", UNSET)

        building_number = d.pop("buildingNumber", UNSET)

        address = d.pop("address", UNSET)

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

        zip_code = d.pop("zipCode", UNSET)

        zip_code_suffix = d.pop("zipCodeSuffix", UNSET)

        location = cls(
            name=name,
            room_number=room_number,
            building_number=building_number,
            address=address,
            city=city,
            state_province=state_province,
            country=country,
            zip_code=zip_code,
            zip_code_suffix=zip_code_suffix,
        )

        location.additional_properties = d
        return location

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
