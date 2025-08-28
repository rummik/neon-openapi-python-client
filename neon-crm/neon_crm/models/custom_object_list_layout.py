from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_object_layout_list_field import CustomObjectLayoutListField


T = TypeVar("T", bound="CustomObjectListLayout")


@_attrs_define
class CustomObjectListLayout:
    """
    Attributes:
        layout_name (Union[Unset, str]):
        is_default (Union[Unset, bool]):
        search_criteria_fields (Union[Unset, CustomObjectLayoutListField]):
        list_fields (Union[Unset, CustomObjectLayoutListField]):
    """

    layout_name: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    search_criteria_fields: Union[Unset, "CustomObjectLayoutListField"] = UNSET
    list_fields: Union[Unset, "CustomObjectLayoutListField"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout_name = self.layout_name

        is_default = self.is_default

        search_criteria_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.search_criteria_fields, Unset):
            search_criteria_fields = self.search_criteria_fields.to_dict()

        list_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.list_fields, Unset):
            list_fields = self.list_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout_name is not UNSET:
            field_dict["layoutName"] = layout_name
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if search_criteria_fields is not UNSET:
            field_dict["searchCriteriaFields"] = search_criteria_fields
        if list_fields is not UNSET:
            field_dict["listFields"] = list_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_object_layout_list_field import CustomObjectLayoutListField

        d = dict(src_dict)
        layout_name = d.pop("layoutName", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _search_criteria_fields = d.pop("searchCriteriaFields", UNSET)
        search_criteria_fields: Union[Unset, CustomObjectLayoutListField]
        if isinstance(_search_criteria_fields, Unset):
            search_criteria_fields = UNSET
        else:
            search_criteria_fields = CustomObjectLayoutListField.from_dict(_search_criteria_fields)

        _list_fields = d.pop("listFields", UNSET)
        list_fields: Union[Unset, CustomObjectLayoutListField]
        if isinstance(_list_fields, Unset):
            list_fields = UNSET
        else:
            list_fields = CustomObjectLayoutListField.from_dict(_list_fields)

        custom_object_list_layout = cls(
            layout_name=layout_name,
            is_default=is_default,
            search_criteria_fields=search_criteria_fields,
            list_fields=list_fields,
        )

        custom_object_list_layout.additional_properties = d
        return custom_object_list_layout

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
