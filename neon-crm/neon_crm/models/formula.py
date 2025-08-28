from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.formula_empty_field_treat_as import FormulaEmptyFieldTreatAs
from ..models.formula_return_data_type import FormulaReturnDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Formula")


@_attrs_define
class Formula:
    """
    Attributes:
        return_data_type (Union[Unset, FormulaReturnDataType]):
        return_data_decimal_length (Union[Unset, int]):
        empty_field_treat_as (Union[Unset, FormulaEmptyFieldTreatAs]):
        formula_expression (Union[Unset, str]):
    """

    return_data_type: Union[Unset, FormulaReturnDataType] = UNSET
    return_data_decimal_length: Union[Unset, int] = UNSET
    empty_field_treat_as: Union[Unset, FormulaEmptyFieldTreatAs] = UNSET
    formula_expression: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return_data_type: Union[Unset, str] = UNSET
        if not isinstance(self.return_data_type, Unset):
            return_data_type = self.return_data_type.value

        return_data_decimal_length = self.return_data_decimal_length

        empty_field_treat_as: Union[Unset, str] = UNSET
        if not isinstance(self.empty_field_treat_as, Unset):
            empty_field_treat_as = self.empty_field_treat_as.value

        formula_expression = self.formula_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if return_data_type is not UNSET:
            field_dict["returnDataType"] = return_data_type
        if return_data_decimal_length is not UNSET:
            field_dict["returnDataDecimalLength"] = return_data_decimal_length
        if empty_field_treat_as is not UNSET:
            field_dict["emptyFieldTreatAs"] = empty_field_treat_as
        if formula_expression is not UNSET:
            field_dict["formulaExpression"] = formula_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _return_data_type = d.pop("returnDataType", UNSET)
        return_data_type: Union[Unset, FormulaReturnDataType]
        if isinstance(_return_data_type, Unset):
            return_data_type = UNSET
        else:
            return_data_type = FormulaReturnDataType(_return_data_type)

        return_data_decimal_length = d.pop("returnDataDecimalLength", UNSET)

        _empty_field_treat_as = d.pop("emptyFieldTreatAs", UNSET)
        empty_field_treat_as: Union[Unset, FormulaEmptyFieldTreatAs]
        if isinstance(_empty_field_treat_as, Unset):
            empty_field_treat_as = UNSET
        else:
            empty_field_treat_as = FormulaEmptyFieldTreatAs(_empty_field_treat_as)

        formula_expression = d.pop("formulaExpression", UNSET)

        formula = cls(
            return_data_type=return_data_type,
            return_data_decimal_length=return_data_decimal_length,
            empty_field_treat_as=empty_field_treat_as,
            formula_expression=formula_expression,
        )

        formula.additional_properties = d
        return formula

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
