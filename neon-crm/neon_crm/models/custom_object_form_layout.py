from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_object_layout_list_field import CustomObjectLayoutListField
    from ..models.custom_object_relation_list import CustomObjectRelationList


T = TypeVar("T", bound="CustomObjectFormLayout")


@_attrs_define
class CustomObjectFormLayout:
    """
    Attributes:
        layout_name (Union[Unset, str]):
        is_default (Union[Unset, bool]):
        form_fields (Union[Unset, CustomObjectLayoutListField]):
        child_tables (Union[Unset, CustomObjectRelationList]):
    """

    layout_name: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    form_fields: Union[Unset, "CustomObjectLayoutListField"] = UNSET
    child_tables: Union[Unset, "CustomObjectRelationList"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout_name = self.layout_name

        is_default = self.is_default

        form_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.form_fields, Unset):
            form_fields = self.form_fields.to_dict()

        child_tables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.child_tables, Unset):
            child_tables = self.child_tables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout_name is not UNSET:
            field_dict["layoutName"] = layout_name
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if form_fields is not UNSET:
            field_dict["formFields"] = form_fields
        if child_tables is not UNSET:
            field_dict["childTables"] = child_tables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_object_layout_list_field import CustomObjectLayoutListField
        from ..models.custom_object_relation_list import CustomObjectRelationList

        d = dict(src_dict)
        layout_name = d.pop("layoutName", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _form_fields = d.pop("formFields", UNSET)
        form_fields: Union[Unset, CustomObjectLayoutListField]
        if isinstance(_form_fields, Unset):
            form_fields = UNSET
        else:
            form_fields = CustomObjectLayoutListField.from_dict(_form_fields)

        _child_tables = d.pop("childTables", UNSET)
        child_tables: Union[Unset, CustomObjectRelationList]
        if isinstance(_child_tables, Unset):
            child_tables = UNSET
        else:
            child_tables = CustomObjectRelationList.from_dict(_child_tables)

        custom_object_form_layout = cls(
            layout_name=layout_name,
            is_default=is_default,
            form_fields=form_fields,
            child_tables=child_tables,
        )

        custom_object_form_layout.additional_properties = d
        return custom_object_form_layout

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
