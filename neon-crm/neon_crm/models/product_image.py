from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductImage")


@_attrs_define
class ProductImage:
    """
    Attributes:
        sequence_id (Union[Unset, int]):
        url (Union[Unset, str]):
        label (Union[Unset, str]):
    """

    sequence_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sequence_id = self.sequence_id

        url = self.url

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sequence_id is not UNSET:
            field_dict["sequenceId"] = sequence_id
        if url is not UNSET:
            field_dict["url"] = url
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sequence_id = d.pop("sequenceId", UNSET)

        url = d.pop("url", UNSET)

        label = d.pop("label", UNSET)

        product_image = cls(
            sequence_id=sequence_id,
            url=url,
            label=label,
        )

        product_image.additional_properties = d
        return product_image

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
