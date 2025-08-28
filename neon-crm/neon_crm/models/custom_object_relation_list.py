from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_object_relation import CustomObjectRelation


T = TypeVar("T", bound="CustomObjectRelationList")


@_attrs_define
class CustomObjectRelationList:
    """
    Attributes:
        custom_object_relation (Union[Unset, list['CustomObjectRelation']]):
    """

    custom_object_relation: Union[Unset, list["CustomObjectRelation"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_object_relation: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_object_relation, Unset):
            custom_object_relation = []
            for custom_object_relation_item_data in self.custom_object_relation:
                custom_object_relation_item = custom_object_relation_item_data.to_dict()
                custom_object_relation.append(custom_object_relation_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_object_relation is not UNSET:
            field_dict["customObjectRelation"] = custom_object_relation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_object_relation import CustomObjectRelation

        d = dict(src_dict)
        custom_object_relation = []
        _custom_object_relation = d.pop("customObjectRelation", UNSET)
        for custom_object_relation_item_data in _custom_object_relation or []:
            custom_object_relation_item = CustomObjectRelation.from_dict(custom_object_relation_item_data)

            custom_object_relation.append(custom_object_relation_item)

        custom_object_relation_list = cls(
            custom_object_relation=custom_object_relation,
        )

        custom_object_relation_list.additional_properties = d
        return custom_object_relation_list

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
