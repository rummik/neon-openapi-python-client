from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Origin")


@_attrs_define
class Origin:
    """
    Attributes:
        origin_detail (Union[Unset, str]):
        origin_category (Union[Unset, str]):
    """

    origin_detail: Union[Unset, str] = UNSET
    origin_category: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        origin_detail = self.origin_detail

        origin_category = self.origin_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origin_detail is not UNSET:
            field_dict["originDetail"] = origin_detail
        if origin_category is not UNSET:
            field_dict["originCategory"] = origin_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        origin_detail = d.pop("originDetail", UNSET)

        origin_category = d.pop("originCategory", UNSET)

        origin = cls(
            origin_detail=origin_detail,
            origin_category=origin_category,
        )

        origin.additional_properties = d
        return origin

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
