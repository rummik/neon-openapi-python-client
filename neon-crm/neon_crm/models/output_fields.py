from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField


T = TypeVar("T", bound="OutputFields")


@_attrs_define
class OutputFields:
    """
    Attributes:
        standard_fields (Union[Unset, list[str]]):
        custom_fields (Union[Unset, list['CustomField']]):
    """

    standard_fields: Union[Unset, list[str]] = UNSET
    custom_fields: Union[Unset, list["CustomField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.standard_fields, Unset):
            standard_fields = self.standard_fields

        custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if standard_fields is not UNSET:
            field_dict["standardFields"] = standard_fields
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field import CustomField

        d = dict(src_dict)
        standard_fields = cast(list[str], d.pop("standardFields", UNSET))

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        output_fields = cls(
            standard_fields=standard_fields,
            custom_fields=custom_fields,
        )

        output_fields.additional_properties = d
        return output_fields

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
