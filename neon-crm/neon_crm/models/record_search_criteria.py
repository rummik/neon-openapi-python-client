from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_search_criteria_operator import RecordSearchCriteriaOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordSearchCriteria")


@_attrs_define
class RecordSearchCriteria:
    """
    Attributes:
        criteria_field (Union[Unset, str]):
        operator (Union[Unset, RecordSearchCriteriaOperator]):
        value (Union[Unset, str]):
        value_list (Union[Unset, list[str]]):
    """

    criteria_field: Union[Unset, str] = UNSET
    operator: Union[Unset, RecordSearchCriteriaOperator] = UNSET
    value: Union[Unset, str] = UNSET
    value_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criteria_field = self.criteria_field

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        value = self.value

        value_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.value_list, Unset):
            value_list = self.value_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria_field is not UNSET:
            field_dict["criteriaField"] = criteria_field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value
        if value_list is not UNSET:
            field_dict["valueList"] = value_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        criteria_field = d.pop("criteriaField", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, RecordSearchCriteriaOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = RecordSearchCriteriaOperator(_operator)

        value = d.pop("value", UNSET)

        value_list = cast(list[str], d.pop("valueList", UNSET))

        record_search_criteria = cls(
            criteria_field=criteria_field,
            operator=operator,
            value=value,
            value_list=value_list,
        )

        record_search_criteria.additional_properties = d
        return record_search_criteria

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
