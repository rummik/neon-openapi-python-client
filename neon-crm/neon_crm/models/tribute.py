from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tribute_type import TributeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tribute")


@_attrs_define
class Tribute:
    """
    Attributes:
        name (Union[Unset, str]):
        type_ (Union[Unset, TributeType]):
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, TributeType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TributeType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TributeType(_type_)

        tribute = cls(
            name=name,
            type_=type_,
        )

        tribute.additional_properties = d
        return tribute

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
