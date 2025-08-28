from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomObjectRelation")


@_attrs_define
class CustomObjectRelation:
    """
    Attributes:
        object_api_name (Union[Unset, str]):
        object_label (Union[Unset, str]):
        relation_id (Union[Unset, int]):
        relate_list_label (Union[Unset, str]):
    """

    object_api_name: Union[Unset, str] = UNSET
    object_label: Union[Unset, str] = UNSET
    relation_id: Union[Unset, int] = UNSET
    relate_list_label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_api_name = self.object_api_name

        object_label = self.object_label

        relation_id = self.relation_id

        relate_list_label = self.relate_list_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_api_name is not UNSET:
            field_dict["objectApiName"] = object_api_name
        if object_label is not UNSET:
            field_dict["objectLabel"] = object_label
        if relation_id is not UNSET:
            field_dict["relationId"] = relation_id
        if relate_list_label is not UNSET:
            field_dict["relateListLabel"] = relate_list_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_api_name = d.pop("objectApiName", UNSET)

        object_label = d.pop("objectLabel", UNSET)

        relation_id = d.pop("relationId", UNSET)

        relate_list_label = d.pop("relateListLabel", UNSET)

        custom_object_relation = cls(
            object_api_name=object_api_name,
            object_label=object_label,
            relation_id=relation_id,
            relate_list_label=relate_list_label,
        )

        custom_object_relation.additional_properties = d
        return custom_object_relation

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
