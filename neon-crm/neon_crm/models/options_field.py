from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_option_value import FieldOptionValue


T = TypeVar("T", bound="OptionsField")


@_attrs_define
class OptionsField:
    """
    Attributes:
        is_required (Union[Unset, bool]):
        field_option_values (Union[Unset, list['FieldOptionValue']]):
    """

    is_required: Union[Unset, bool] = UNSET
    field_option_values: Union[Unset, list["FieldOptionValue"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_required = self.is_required

        field_option_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.field_option_values, Unset):
            field_option_values = []
            for field_option_values_item_data in self.field_option_values:
                field_option_values_item = field_option_values_item_data.to_dict()
                field_option_values.append(field_option_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if field_option_values is not UNSET:
            field_dict["fieldOptionValues"] = field_option_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_option_value import FieldOptionValue

        d = dict(src_dict)
        is_required = d.pop("isRequired", UNSET)

        field_option_values = []
        _field_option_values = d.pop("fieldOptionValues", UNSET)
        for field_option_values_item_data in _field_option_values or []:
            field_option_values_item = FieldOptionValue.from_dict(field_option_values_item_data)

            field_option_values.append(field_option_values_item)

        options_field = cls(
            is_required=is_required,
            field_option_values=field_option_values,
        )

        options_field.additional_properties = d
        return options_field

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
