from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_custom_field_operators_item import SearchCustomFieldOperatorsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCustomField")


@_attrs_define
class SearchCustomField:
    """
    Attributes:
        display_name (Union[Unset, str]):
        operators (Union[Unset, list[SearchCustomFieldOperatorsItem]]):
        id (Union[Unset, int]):
    """

    display_name: Union[Unset, str] = UNSET
    operators: Union[Unset, list[SearchCustomFieldOperatorsItem]] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        operators: Union[Unset, list[str]] = UNSET
        if not isinstance(self.operators, Unset):
            operators = []
            for operators_item_data in self.operators:
                operators_item = operators_item_data.value
                operators.append(operators_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if operators is not UNSET:
            field_dict["operators"] = operators
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        operators = []
        _operators = d.pop("operators", UNSET)
        for operators_item_data in _operators or []:
            operators_item = SearchCustomFieldOperatorsItem(operators_item_data)

            operators.append(operators_item)

        id = d.pop("id", UNSET)

        search_custom_field = cls(
            display_name=display_name,
            operators=operators,
            id=id,
        )

        search_custom_field.additional_properties = d
        return search_custom_field

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
