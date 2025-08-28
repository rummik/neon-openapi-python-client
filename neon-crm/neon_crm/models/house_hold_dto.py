from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.house_hold_contact_dto import HouseHoldContactDto


T = TypeVar("T", bound="HouseHoldDto")


@_attrs_define
class HouseHoldDto:
    """
    Attributes:
        name (str):
        contacts (list['HouseHoldContactDto']):
        id (Union[Unset, str]):
        salutation (Union[Unset, str]):
    """

    name: str
    contacts: list["HouseHoldContactDto"]
    id: Union[Unset, str] = UNSET
    salutation: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        contacts = []
        for contacts_item_data in self.contacts:
            contacts_item = contacts_item_data.to_dict()
            contacts.append(contacts_item)

        id = self.id

        salutation = self.salutation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "contacts": contacts,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if salutation is not UNSET:
            field_dict["salutation"] = salutation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.house_hold_contact_dto import HouseHoldContactDto

        d = dict(src_dict)
        name = d.pop("name")

        contacts = []
        _contacts = d.pop("contacts")
        for contacts_item_data in _contacts:
            contacts_item = HouseHoldContactDto.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        id = d.pop("id", UNSET)

        salutation = d.pop("salutation", UNSET)

        house_hold_dto = cls(
            name=name,
            contacts=contacts,
            id=id,
            salutation=salutation,
        )

        house_hold_dto.additional_properties = d
        return house_hold_dto

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
