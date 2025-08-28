from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_criteria_operator import SearchCriteriaOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_criteria_value_list_item import SearchCriteriaValueListItem


T = TypeVar("T", bound="SearchCriteria")


@_attrs_define
class SearchCriteria:
    """
    Attributes:
        field (Union[Unset, str]):
        operator (Union[Unset, SearchCriteriaOperator]):
        value (Union[Unset, str]):
        value_list (Union[Unset, list['SearchCriteriaValueListItem']]):
    """

    field: Union[Unset, str] = UNSET
    operator: Union[Unset, SearchCriteriaOperator] = UNSET
    value: Union[Unset, str] = UNSET
    value_list: Union[Unset, list["SearchCriteriaValueListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        value = self.value

        value_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.value_list, Unset):
            value_list = []
            for value_list_item_data in self.value_list:
                value_list_item = value_list_item_data.to_dict()
                value_list.append(value_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value
        if value_list is not UNSET:
            field_dict["valueList"] = value_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_criteria_value_list_item import SearchCriteriaValueListItem

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, SearchCriteriaOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = SearchCriteriaOperator(_operator)

        value = d.pop("value", UNSET)

        value_list = []
        _value_list = d.pop("valueList", UNSET)
        for value_list_item_data in _value_list or []:
            value_list_item = SearchCriteriaValueListItem.from_dict(value_list_item_data)

            value_list.append(value_list_item)

        search_criteria = cls(
            field=field,
            operator=operator,
            value=value,
            value_list=value_list,
        )

        search_criteria.additional_properties = d
        return search_criteria

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
