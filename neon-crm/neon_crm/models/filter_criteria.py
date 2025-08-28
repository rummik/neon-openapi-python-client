from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterCriteria")


@_attrs_define
class FilterCriteria:
    """
    Attributes:
        criteria_field (Union[Unset, str]):
        operator (Union[Unset, str]):
        type_ (Union[Unset, str]):
        search_field (Union[Unset, str]):
        search_value (Union[Unset, str]):
        group_id (Union[Unset, str]):
    """

    criteria_field: Union[Unset, str] = UNSET
    operator: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    search_field: Union[Unset, str] = UNSET
    search_value: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criteria_field = self.criteria_field

        operator = self.operator

        type_ = self.type_

        search_field = self.search_field

        search_value = self.search_value

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria_field is not UNSET:
            field_dict["criteriaField"] = criteria_field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if type_ is not UNSET:
            field_dict["type"] = type_
        if search_field is not UNSET:
            field_dict["searchField"] = search_field
        if search_value is not UNSET:
            field_dict["searchValue"] = search_value
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        criteria_field = d.pop("criteriaField", UNSET)

        operator = d.pop("operator", UNSET)

        type_ = d.pop("type", UNSET)

        search_field = d.pop("searchField", UNSET)

        search_value = d.pop("searchValue", UNSET)

        group_id = d.pop("groupId", UNSET)

        filter_criteria = cls(
            criteria_field=criteria_field,
            operator=operator,
            type_=type_,
            search_field=search_field,
            search_value=search_value,
            group_id=group_id,
        )

        filter_criteria.additional_properties = d
        return filter_criteria

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
