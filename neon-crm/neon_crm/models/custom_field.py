from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """
    Attributes:
        id (Union[Unset, str]):
        value (Union[Unset, str]):
        name (Union[Unset, str]):
        option_values (Union[Unset, list['IdNamePair']]):
    """

    id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    option_values: Union[Unset, list["IdNamePair"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        name = self.name

        option_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.option_values, Unset):
            option_values = []
            for option_values_item_data in self.option_values:
                option_values_item = option_values_item_data.to_dict()
                option_values.append(option_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if name is not UNSET:
            field_dict["name"] = name
        if option_values is not UNSET:
            field_dict["optionValues"] = option_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        name = d.pop("name", UNSET)

        option_values = []
        _option_values = d.pop("optionValues", UNSET)
        for option_values_item_data in _option_values or []:
            option_values_item = IdNamePair.from_dict(option_values_item_data)

            option_values.append(option_values_item)

        custom_field = cls(
            id=id,
            value=value,
            name=name,
            option_values=option_values,
        )

        custom_field.additional_properties = d
        return custom_field

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
