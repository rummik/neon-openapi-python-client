from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.layout_field import LayoutField


T = TypeVar("T", bound="CustomObjectLayoutListField")


@_attrs_define
class CustomObjectLayoutListField:
    """
    Attributes:
        layout_field (Union[Unset, list['LayoutField']]):
    """

    layout_field: Union[Unset, list["LayoutField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout_field: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.layout_field, Unset):
            layout_field = []
            for layout_field_item_data in self.layout_field:
                layout_field_item = layout_field_item_data.to_dict()
                layout_field.append(layout_field_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout_field is not UNSET:
            field_dict["layoutField"] = layout_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_field import LayoutField

        d = dict(src_dict)
        layout_field = []
        _layout_field = d.pop("layoutField", UNSET)
        for layout_field_item_data in _layout_field or []:
            layout_field_item = LayoutField.from_dict(layout_field_item_data)

            layout_field.append(layout_field_item)

        custom_object_layout_list_field = cls(
            layout_field=layout_field,
        )

        custom_object_layout_list_field.additional_properties = d
        return custom_object_layout_list_field

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
