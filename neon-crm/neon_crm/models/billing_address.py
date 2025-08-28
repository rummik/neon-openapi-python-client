from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog import Catalog
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="BillingAddress")


@_attrs_define
class BillingAddress:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):
        address_line_2 (Union[Unset, str]):
        city (Union[Unset, str]):
        state_province_code (Union[Unset, str]):
        territory (Union[Unset, str]):
        country_id (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        zip_code_suffix (Union[Unset, str]):
        catalog (Union[Unset, Catalog]):
        id_name_pairs (Union[Unset, list['IdNamePair']]):
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_province_code: Union[Unset, str] = UNSET
    territory: Union[Unset, str] = UNSET
    country_id: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    zip_code_suffix: Union[Unset, str] = UNSET
    catalog: Union[Unset, "Catalog"] = UNSET
    id_name_pairs: Union[Unset, list["IdNamePair"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        city = self.city

        state_province_code = self.state_province_code

        territory = self.territory

        country_id = self.country_id

        zip_code = self.zip_code

        zip_code_suffix = self.zip_code_suffix

        catalog: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.catalog, Unset):
            catalog = self.catalog.to_dict()

        id_name_pairs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.id_name_pairs, Unset):
            id_name_pairs = []
            for id_name_pairs_item_data in self.id_name_pairs:
                id_name_pairs_item = id_name_pairs_item_data.to_dict()
                id_name_pairs.append(id_name_pairs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if city is not UNSET:
            field_dict["city"] = city
        if state_province_code is not UNSET:
            field_dict["stateProvinceCode"] = state_province_code
        if territory is not UNSET:
            field_dict["territory"] = territory
        if country_id is not UNSET:
            field_dict["countryId"] = country_id
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if zip_code_suffix is not UNSET:
            field_dict["zipCodeSuffix"] = zip_code_suffix
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if id_name_pairs is not UNSET:
            field_dict["idNamePairs"] = id_name_pairs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog import Catalog
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        city = d.pop("city", UNSET)

        state_province_code = d.pop("stateProvinceCode", UNSET)

        territory = d.pop("territory", UNSET)

        country_id = d.pop("countryId", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        zip_code_suffix = d.pop("zipCodeSuffix", UNSET)

        _catalog = d.pop("catalog", UNSET)
        catalog: Union[Unset, Catalog]
        if isinstance(_catalog, Unset):
            catalog = UNSET
        else:
            catalog = Catalog.from_dict(_catalog)

        id_name_pairs = []
        _id_name_pairs = d.pop("idNamePairs", UNSET)
        for id_name_pairs_item_data in _id_name_pairs or []:
            id_name_pairs_item = IdNamePair.from_dict(id_name_pairs_item_data)

            id_name_pairs.append(id_name_pairs_item)

        billing_address = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state_province_code=state_province_code,
            territory=territory,
            country_id=country_id,
            zip_code=zip_code,
            zip_code_suffix=zip_code_suffix,
            catalog=catalog,
            id_name_pairs=id_name_pairs,
        )

        billing_address.additional_properties = d
        return billing_address

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
