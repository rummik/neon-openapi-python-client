from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_type_id import ProductTypeId


T = TypeVar("T", bound="ProductCustomFieldData")


@_attrs_define
class ProductCustomFieldData:
    """
    Attributes:
        show_on_product_detail (Union[Unset, bool]):
        show_on_storefront (Union[Unset, bool]):
        product_types (Union[Unset, list['ProductTypeId']]):
    """

    show_on_product_detail: Union[Unset, bool] = UNSET
    show_on_storefront: Union[Unset, bool] = UNSET
    product_types: Union[Unset, list["ProductTypeId"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        show_on_product_detail = self.show_on_product_detail

        show_on_storefront = self.show_on_storefront

        product_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_types, Unset):
            product_types = []
            for product_types_item_data in self.product_types:
                product_types_item = product_types_item_data.to_dict()
                product_types.append(product_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if show_on_product_detail is not UNSET:
            field_dict["showOnProductDetail"] = show_on_product_detail
        if show_on_storefront is not UNSET:
            field_dict["showOnStorefront"] = show_on_storefront
        if product_types is not UNSET:
            field_dict["productTypes"] = product_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_type_id import ProductTypeId

        d = dict(src_dict)
        show_on_product_detail = d.pop("showOnProductDetail", UNSET)

        show_on_storefront = d.pop("showOnStorefront", UNSET)

        product_types = []
        _product_types = d.pop("productTypes", UNSET)
        for product_types_item_data in _product_types or []:
            product_types_item = ProductTypeId.from_dict(product_types_item_data)

            product_types.append(product_types_item)

        product_custom_field_data = cls(
            show_on_product_detail=show_on_product_detail,
            show_on_storefront=show_on_storefront,
            product_types=product_types,
        )

        product_custom_field_data.additional_properties = d
        return product_custom_field_data

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
