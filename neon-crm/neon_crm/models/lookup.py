from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relation_filter import RelationFilter


T = TypeVar("T", bound="Lookup")


@_attrs_define
class Lookup:
    """
    Attributes:
        related_object_api_name (Union[Unset, str]):
        reparent_allow (Union[Unset, bool]):
        relation_filter (Union[Unset, RelationFilter]):
        add_system_related_list (Union[Unset, bool]):
        related_list_label (Union[Unset, str]):
    """

    related_object_api_name: Union[Unset, str] = UNSET
    reparent_allow: Union[Unset, bool] = UNSET
    relation_filter: Union[Unset, "RelationFilter"] = UNSET
    add_system_related_list: Union[Unset, bool] = UNSET
    related_list_label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        related_object_api_name = self.related_object_api_name

        reparent_allow = self.reparent_allow

        relation_filter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relation_filter, Unset):
            relation_filter = self.relation_filter.to_dict()

        add_system_related_list = self.add_system_related_list

        related_list_label = self.related_list_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if related_object_api_name is not UNSET:
            field_dict["relatedObjectApiName"] = related_object_api_name
        if reparent_allow is not UNSET:
            field_dict["reparentAllow"] = reparent_allow
        if relation_filter is not UNSET:
            field_dict["relationFilter"] = relation_filter
        if add_system_related_list is not UNSET:
            field_dict["addSystemRelatedList"] = add_system_related_list
        if related_list_label is not UNSET:
            field_dict["relatedListLabel"] = related_list_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relation_filter import RelationFilter

        d = dict(src_dict)
        related_object_api_name = d.pop("relatedObjectApiName", UNSET)

        reparent_allow = d.pop("reparentAllow", UNSET)

        _relation_filter = d.pop("relationFilter", UNSET)
        relation_filter: Union[Unset, RelationFilter]
        if isinstance(_relation_filter, Unset):
            relation_filter = UNSET
        else:
            relation_filter = RelationFilter.from_dict(_relation_filter)

        add_system_related_list = d.pop("addSystemRelatedList", UNSET)

        related_list_label = d.pop("relatedListLabel", UNSET)

        lookup = cls(
            related_object_api_name=related_object_api_name,
            reparent_allow=reparent_allow,
            relation_filter=relation_filter,
            add_system_related_list=add_system_related_list,
            related_list_label=related_list_label,
        )

        lookup.additional_properties = d
        return lookup

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
