from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_option_status import ProductOptionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_option_item import ProductOptionItem


T = TypeVar("T", bound="ProductOption")


@_attrs_define
class ProductOption:
    """
    Attributes:
        id (Union[Unset, str]):
        items (Union[Unset, list['ProductOptionItem']]):
        name (Union[Unset, str]):
        status (Union[Unset, ProductOptionStatus]):
    """

    id: Union[Unset, str] = UNSET
    items: Union[Unset, list["ProductOptionItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ProductOptionStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_option_item import ProductOptionItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = ProductOptionItem.from_dict(items_item_data)

            items.append(items_item)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProductOptionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProductOptionStatus(_status)

        product_option = cls(
            id=id,
            items=items,
            name=name,
            status=status,
        )

        product_option.additional_properties = d
        return product_option

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
