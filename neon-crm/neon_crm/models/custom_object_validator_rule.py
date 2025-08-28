from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomObjectValidatorRule")


@_attrs_define
class CustomObjectValidatorRule:
    """
    Attributes:
        validator_name (Union[Unset, str]):
        error_message (Union[Unset, str]):
        description (Union[Unset, str]):
        validator_expression (Union[Unset, str]):
        is_active (Union[Unset, bool]):
    """

    validator_name: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    validator_expression: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        validator_name = self.validator_name

        error_message = self.error_message

        description = self.description

        validator_expression = self.validator_expression

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validator_name is not UNSET:
            field_dict["validatorName"] = validator_name
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if description is not UNSET:
            field_dict["description"] = description
        if validator_expression is not UNSET:
            field_dict["validatorExpression"] = validator_expression
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        validator_name = d.pop("validatorName", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        description = d.pop("description", UNSET)

        validator_expression = d.pop("validatorExpression", UNSET)

        is_active = d.pop("isActive", UNSET)

        custom_object_validator_rule = cls(
            validator_name=validator_name,
            error_message=error_message,
            description=description,
            validator_expression=validator_expression,
            is_active=is_active,
        )

        custom_object_validator_rule.additional_properties = d
        return custom_object_validator_rule

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
