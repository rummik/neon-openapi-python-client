from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_field_operators_item import StandardFieldOperatorsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="StandardField")


@_attrs_define
class StandardField:
    """
    Attributes:
        field_name (Union[Unset, str]):
        operators (Union[Unset, list[StandardFieldOperatorsItem]]):
    """

    field_name: Union[Unset, str] = UNSET
    operators: Union[Unset, list[StandardFieldOperatorsItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        operators: Union[Unset, list[str]] = UNSET
        if not isinstance(self.operators, Unset):
            operators = []
            for operators_item_data in self.operators:
                operators_item = operators_item_data.value
                operators.append(operators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if operators is not UNSET:
            field_dict["operators"] = operators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("fieldName", UNSET)

        operators = []
        _operators = d.pop("operators", UNSET)
        for operators_item_data in _operators or []:
            operators_item = StandardFieldOperatorsItem(operators_item_data)

            operators.append(operators_item)

        standard_field = cls(
            field_name=field_name,
            operators=operators,
        )

        standard_field.additional_properties = d
        return standard_field

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
